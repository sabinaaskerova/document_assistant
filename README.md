# RAG Document Assistant

A Retrieval-Augmented Generation (RAG) system that enables users to ask questions about their documents and receive accurate, context-aware answers. The system uses local language models through Ollama for inference.

## Features

- PDF document processing and text extraction
- Text chunking and embedding generation
- Vector similarity search using FAISS
- Integration with local LLMs through Ollama
- Web interface built with Streamlit

## Requirements

- Python 3.9+
- Ollama (with llama2 or other model installed)
- Docker
## Environment Setup

### 1. Local Setup

1. Clone the repository:
```bash
git clone https://github.com/sabinaaskerova/document_assistant.git
cd document_assistant
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Install and start Ollama:
```bash
# Install Ollama from https://ollama.ai/
# Pull the llama2 model or any other model if you wish
ollama pull llama2
```

### 2. Docker Setup

1. Build the Docker image:
```bash
docker build -t rag-assistant .
```

2. Run the container:
```bash
docker run -p 8501:8501 rag-assistant
```

## Usage

### Running the Application

1. Start the Streamlit app:
```bash
streamlit run src/app.py
```

2. Open your browser and navigate to:
```
http://localhost:8501
```
### Example Usage

Let's say you have a technical manual `manual.pdf` and want to ask questions about it:

1. Upload the PDF through the web interface
2. Wait for the processing to complete
3. Ask your questions in the text input field

Example questions:
- "What are the system requirements?"
- "How do I troubleshoot network connectivity issues?"
- "What is the recommended maintenance schedule?"
