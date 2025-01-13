import fitz  # For extracting text from PDF 

def extract_text_from_pdf(pdf_path):
    """Extract text content from a PDF file."""
    doc = fitz.open(pdf_path)
    texts = []
    
    for page in doc:
        texts.append(page.get_text())
        
    doc.close()
    return texts