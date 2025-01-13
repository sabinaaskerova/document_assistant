from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
# from langchain_community.llms import Ollama
from langchain_ollama import OllamaLLM
from langchain.prompts import PromptTemplate
from langchain_huggingface import HuggingFaceEmbeddings 

class RAGSystem:
    def __init__(self, model_name="llama2"):
        self.embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-mpnet-base-v2", # Embedding model
            model_kwargs={'device': 'cpu'}  # Explicitly set device to avoid torch warnings
        )
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
        )
        self.llm = OllamaLLM(model=model_name)
        self.vector_store = None
        
    def ingest_document(self, texts):
        """Process and store document chunks in the vector store."""
        chunks = self.text_splitter.split_text("\n".join(texts))
        self.vector_store = FAISS.from_texts(chunks, self.embeddings)
        
    def get_retriever(self):
        """Get the retriever component."""
        if not self.vector_store:
            raise ValueError("No documents have been ingested yet.")
        return self.vector_store.as_retriever(
            search_type="similarity",
            search_kwargs={"k": 3}
        )
        
    def get_qa_chain(self):
        """Create a question-answering chain."""
        prompt_template = """Use the following pieces of context to answer the question. 
        If you don't know the answer, just say you don't know.
        
        Context: {context}
        
        Question: {question}
        
        Answer:"""
        
        prompt = PromptTemplate(
            template=prompt_template,
            input_variables=["context", "question"]
        )
        
        chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=self.get_retriever(),
            chain_type_kwargs={"prompt": prompt},
            return_source_documents=True
        )
        return chain
