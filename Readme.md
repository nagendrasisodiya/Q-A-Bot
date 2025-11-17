# Gradio Q&A Bot - Learning Project

A practical learning project exploring Gradio interface development with IBM Watsonx AI integration. This repository contains multiple Gradio demos and functional chatbots, including an advanced RAG-powered PDF Q&A system using IBM's Granite language model.

## 📋 Project Overview

This project demonstrates:
- Building interactive web interfaces with Gradio
- Integrating IBM Watsonx AI for LLM-powered applications
- Implementing Retrieval Augmented Generation (RAG) for document-based Q&A
- Progressive learning from simple to complex Gradio implementations
- Creating production-ready chatbot interfaces with vector database integration

## 🗂️ Project Structure

```
Gradio-QABot/
├── .gradio/                   # Gradio cache directory
├── .venv/                     # Python virtual environment (library root)
├── LLM/
│   ├── .gradio/
│   ├── .env                   # Environment variables (API keys)
│   ├── simple_llm.py          # Basic LLM CLI implementation
│   └── simple_gradio_llm.py   # Gradio-powered chatbot
├── Q&A-Bot/
│   ├── .gradio/
│   ├── .env                   # Environment variables (API keys)
│   └── qabot.py               # RAG-powered PDF Q&A bot ⭐ NEW
├── gradio_demo-01.py          # Demo: Basic number addition
├── gradio_demo-02.py          # Demo: Text combination
├── gradio_demo-03.py          # Demo: Advanced inputs (sliders, dropdowns)
├── .gitignore                 # Git ignore rules
├── Gradio Interface Inputs and Outputs.txt
├── poetry.lock                # Poetry lock file for dependencies
├── poetry.toml                # Poetry configuration
├── pyproject.toml             # Poetry project configuration
└── README.md                  # Project documentation
```

## 🚀 Features

### Gradio Demos
1. **Demo 01** - Simple number addition interface
2. **Demo 02** - Text combination with labeled inputs
3. **Demo 03** - Complex sentence builder with multiple input types:
   - Sliders
   - Dropdowns (single & multi-select)
   - Checkbox groups
   - Radio buttons
   - Pre-configured examples

### Simple Q&A Chatbot
- Powered by IBM Watsonx AI (Granite 3.3 8B Instruct model)
- Clean, user-friendly Gradio interface
- Real-time response generation
- Configurable parameters (temperature, max tokens)

### Advanced PDF Q&A Bot (RAG) ⭐ NEW
The crown jewel of this project - an intelligent document Q&A system that uses Retrieval Augmented Generation:

**Key Features:**
- **PDF Document Upload**: Upload any PDF file through the Gradio interface
- **Intelligent Document Processing**: 
  - Automatic text extraction from PDFs using PyPDFLoader
  - Smart text chunking with RecursiveCharacterTextSplitter (1000 char chunks, 200 char overlap)
  - Preserves context while maintaining manageable chunk sizes
- **Vector Search with ChromaDB**: 
  - Creates embeddings using IBM Watsonx sentence transformer model
  - Stores document chunks in a local ChromaDB vector database
  - Enables semantic similarity search for relevant context retrieval
- **RAG Pipeline**:
  - Retrieves most relevant document chunks based on query
  - Augments LLM prompt with retrieved context
  - Generates accurate, context-aware answers grounded in your documents
- **Source Attribution**: Returns answers with source document references
- **User-Friendly Interface**: Simple upload and ask workflow

**How it Works:**
1. Upload a PDF document
2. System automatically processes and indexes the document
3. Ask any question about the document content
4. Receive accurate answers based on the actual document content

This implementation showcases RAG as a technique that combines retrieval of relevant information from external knowledge sources with generative AI to create accurate, context-grounded responses, making it perfect for question-answering tasks over custom documents.

## 🛠️ Technologies Used

- **Python 3.12+** (< 3.14)
- **Poetry** - Dependency management and packaging
- **Gradio 5.x** - Web UI framework for ML applications
- **LangChain** - LLM application framework and RAG orchestration
- **LangChain-IBM** - IBM Watsonx integration for LangChain
- **IBM Watsonx AI** - Enterprise AI platform
  - Granite 3.3 8B Instruct (main LLM)
  - Sentence Transformers (embedding model)
- **ChromaDB** - Vector database for document embeddings and similarity search
- **PyPDF** - PDF processing and text extraction
- **python-dotenv** - Environment variable management

## 📦 Installation

### Prerequisites
- Python 3.12 or 3.13
- Poetry (install from [python-poetry.org](https://python-poetry.org/docs/#installation))
- IBM Watsonx AI account and API key

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd Gradio-QABot
   ```

2. **Install dependencies with Poetry**
   ```bash
   poetry install
   ```
   
   Poetry will automatically:
   - Create a virtual environment
   - Install all dependencies from `pyproject.toml`
   - Set up the project for development

3. **Activate the Poetry virtual environment**
   ```bash
   poetry shell
   ```
   
   Or run commands directly with Poetry:
   ```bash
   poetry run python Q&A-Bot/qabot.py
   ```

4. **Set up environment variables**
   
   Create a `.env` file in the `LLM/` directory:
   ```env
   WATSONX_API_KEY=your_api_key_here
   ```
   
   Get your API key from [IBM Watsonx](https://www.ibm.com/watsonx)

## 🎯 Usage

### Running Gradio Demos

```bash
# Using Poetry shell
poetry shell

# Demo 01 - Number addition
python gradio_demo-01.py

# Demo 02 - Text combination
python gradio_demo-02.py

# Demo 03 - Sentence builder
python gradio_demo-03.py
```

Or run directly without activating shell:
```bash
poetry run python gradio_demo-01.py
```

### Running the Simple Q&A Chatbot

**CLI Version:**
```bash
poetry run python LLM/simple_llm.py
```

**Gradio Web Interface:**
```bash
poetry run python LLM/simple_gradio_llm.py
```

Then open your browser and navigate to: `http://127.0.0.1:8080`

### Running the Advanced PDF Q&A Bot (RAG) ⭐

```bash
poetry run python Q&A-Bot/qabot.py
```

Then open your browser to: `http://127.0.0.1:8080`

**Usage Instructions:**
1. Click "Upload your PDF file" and select a PDF document
2. Type your question in the "Ask your question" textbox
3. Click Submit to get an AI-generated answer based on your document
4. The bot will process the PDF, find relevant sections, and generate an accurate response

**Tips:**
- Works best with text-based PDFs (not scanned images)
- Ask specific questions for more focused answers
- The system chunks documents intelligently to maintain context
- Answers are grounded in the actual document content, reducing hallucinations

## 📋 Dependencies

All project dependencies are managed through Poetry and defined in `pyproject.toml`:

```toml
[project]
name = "gradio-qabot"
version = "0.1.0"
requires-python = ">=3.12,<3.14"

dependencies = [
    "gradio (>=5.49.1,<6.0.0)",
    "ibm-watsonx-ai (>=1.4.6,<2.0.0)",
    "langchain (>=1.0.7,<2.0.0)",
    "langchain-community (>=0.4.1,<0.5.0)",
    "langchain-ibm (>=1.0.1,<2.0.0)",
    "chromadb (>=1.3.4,<2.0.0)",
    "pypdf (>=6.3.0,<7.0.0)",
    "pydantic (<2.12)",
    "load-dotenv (>=0.1.0,<0.2.0)"
]
```

### Adding New Dependencies
```bash
poetry add package-name
```

### Updating Dependencies
```bash
poetry update
```

## ⚙️ Configuration

### Simple Chatbot Configuration
The simple LLM chatbot is configured in `simple_gradio_llm.py`:

```python
model_id = 'ibm/granite-3-3-8b-instruct'
parameters = {
    GenParams.MAX_NEW_TOKENS: 256,
    GenParams.TEMPERATURE: 0.5,
}
```

### PDF Q&A Bot Configuration
The RAG-powered bot is configured in `qabot.py`:

```python
# LLM Configuration
model_id = 'ibm/granite-3-3-8b-instruct'
parameters = {
    GenParams.MAX_NEW_TOKENS: 256,
    GenParams.TEMPERATURE: 0.5,
}

# Document Processing
chunk_size = 1000          # Size of text chunks
chunk_overlap = 200        # Overlap between chunks

# Embedding Model
embedding_model = "sentence-transformers/all-minilm-l6-v2"
```

**Adjustable Parameters:**
- `MAX_NEW_TOKENS`: Maximum length of generated responses (default: 256)
- `TEMPERATURE`: Controls randomness (0.0 = deterministic, 1.0 = creative)
- `chunk_size`: Size of document chunks for processing
- `chunk_overlap`: Overlap between chunks to preserve context

## 🏗️ Architecture

### RAG Pipeline Flow

```
PDF Upload → Document Loading → Text Splitting → Embedding Generation
                                                          ↓
User Query → Query Embedding → Vector Search → Context Retrieval
                                                          ↓
                              Query + Context → LLM → Generated Answer
```

**Component Breakdown:**
1. **Document Loader**: Extracts text from PDF files
2. **Text Splitter**: Breaks documents into manageable, overlapping chunks
3. **Embedding Model**: Converts text chunks into vector representations
4. **Vector Database (ChromaDB)**: Stores and retrieves document embeddings
5. **Retriever**: Finds most relevant chunks based on query similarity
6. **LLM (Granite)**: Generates answers using retrieved context
7. **RetrievalQA Chain**: Orchestrates the entire RAG pipeline

## 📚 Learning Highlights

### Gradio Input Types Explored
- ✅ Number inputs
- ✅ Textbox (single & multi-line)
- ✅ File upload (PDF)
- ✅ Slider
- ✅ Dropdown (single & multi-select)
- ✅ Checkbox & CheckboxGroup
- ✅ Radio buttons

### Advanced Concepts Implemented
1. **RAG (Retrieval Augmented Generation)**
   - Document indexing and vector storage
   - Semantic similarity search
   - Context-aware answer generation
   - Source attribution

2. **Vector Databases**
   - ChromaDB integration
   - Embedding storage and retrieval
   - Similarity search algorithms

3. **Document Processing**
   - PDF text extraction
   - Intelligent text chunking
   - Context preservation with overlap

4. **LangChain Framework**
   - RetrievalQA chains
   - Document loaders
   - Text splitters
   - Embeddings integration

5. **Production-Ready Features**
   - Error handling
   - Environment variable management
   - Clean user interfaces
   - Modular code architecture

## 🔒 Security Notes

- API keys are stored in `.env` files (excluded from version control)
- Never commit sensitive credentials to the repository
- The `.gitignore` file properly excludes secrets and environment files
- Project ID is included in code for IBM Watsonx integration

## 🚧 Future Improvements

- [x] ~~Add RAG capabilities with ChromaDB~~ ✅ Completed!
- [x] ~~Implement PDF document processing~~ ✅ Completed!
- [ ] Add conversation history/memory to chatbots
- [ ] Implement streaming responses for real-time feedback
- [ ] Support multiple file formats (Word, TXT, Markdown)
- [ ] Add batch document processing
- [ ] Implement document summarization

## 📖 Resources

- [Gradio Documentation](https://www.gradio.app/docs)
- [LangChain Documentation](https://python.langchain.com/)
- [IBM Watsonx AI Documentation](https://www.ibm.com/docs/en/watsonx-as-a-service)
- [ChromaDB Documentation](https://docs.trychroma.com/)
- [RAG from Scratch Tutorial](https://github.com/langchain-ai/rag-from-scratch)

## 💡 Use Cases

This project demonstrates skills applicable to:
- **Enterprise Document Search**: Query internal documentation, policies, and knowledge bases
- **Research Assistance**: Ask questions about research papers and technical documents
- **Customer Support**: Answer customer queries based on product documentation
- **Legal Document Analysis**: Extract information from contracts and legal documents
- **Educational Tools**: Create study aids from textbooks and course materials
- **Content Management**: Build intelligent search for content repositories

## 👨‍💻 Author

Learning and building practical AI applications with Gradio, LangChain, and IBM Watsonx AI. This project showcases progressive learning from basic UI components to advanced RAG implementations.

## 📝 License

This is a learning project. Feel free to use and modify as needed for educational purposes.

---

**Note:** This project requires an IBM Watsonx AI account and API key. Visit [IBM Watsonx](https://www.ibm.com/watsonx) to get started.

**Project Status**: 🟢 Active Development | Last Updated: November 2025