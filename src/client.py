from rag import RAGSystem
from retriever import extract_text_from_pdf

class RAGClient:
    def __init__(self):
        self.rag_system = RAGSystem()
        
    def load_document(self, pdf_path):
        """Load and process a document."""
        texts = extract_text_from_pdf(pdf_path)
        self.rag_system.ingest_document(texts)
        
    def query(self, question):
        """Query the system with a question."""
        qa_chain = self.rag_system.get_qa_chain()
        # Using invoke method to query the system
        response = qa_chain.invoke({"query": question})
        return {
            "answer": response["result"],
            "source_documents": response["source_documents"]
        }