import streamlit as st
from client import RAGClient
import os

st.set_page_config(page_title="Document Q&A Assistant", layout="wide")

@st.cache_resource
def get_rag_client():
    return RAGClient()

def main():
    st.title("Document Q&A Assistant")
    
    client = get_rag_client()
    
    uploaded_file = st.file_uploader("Upload a PDF document", type="pdf")
    
    if uploaded_file:
        # Save uploaded file temporarily
        with open("temp.pdf", "wb") as f:
            f.write(uploaded_file.getvalue())
            
        # Load document
        with st.spinner("Processing document..."):
            client.load_document("temp.pdf")
        st.success("Document processed successfully!")
        
        os.remove("temp.pdf") # Remove temporary file
        
    # Question input
    question = st.text_input("Ask a question about the document:")
    
    if question and uploaded_file:
        with st.spinner("Generating answer..."):
            response = client.query(question)
            
        st.write("### Answer")
        st.write(response["answer"])
        
        st.write("### Source Passages")
        for doc in response["source_documents"]:
            st.text(doc.page_content)

if __name__ == "__main__":
    main()
