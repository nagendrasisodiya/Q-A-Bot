# Gradio Q&A Bot - Learning Project

A practical learning project exploring Gradio interface development with IBM Watsonx AI integration. This repository contains multiple Gradio demos and a functional Q&A chatbot powered by IBM's Granite language model.

## 📋 Project Overview

This project demonstrates:
- Building interactive web interfaces with Gradio
- Integrating IBM Watsonx AI for LLM-powered applications
- Progressive learning from simple to complex Gradio implementations
- Creating a production-ready Q&A chatbot interface

## 🗂️ Project Structure

```
Gradio-QABot/
├── LLM/
│   ├── .gradio/
│   ├── .env                    # Environment variables (API keys)
│   ├── simple_llm.py          # Basic LLM CLI implementation
│   └── simple_gradio_llm.py   # Gradio-powered chatbot
├── Q&A-Bot/                   # Main Q&A bot directory
├── gradio_demo-01.py          # Demo: Basic number addition
├── gradio_demo-02.py          # Demo: Text combination
├── gradio_demo-03.py          # Demo: Advanced inputs (sliders, dropdowns)
├── pyproject.toml             # Poetry project configuration
├── poetry.lock                # Lock file for dependencies (not in git)
├── Gradio Interface Inputs and Outputs.txt
├── .gitignore
└── README.md
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

### Q&A Chatbot
- Powered by IBM Watsonx AI (Granite 3.3 8B Instruct model)
- Clean, user-friendly Gradio interface
- Real-time response generation
- Configurable parameters (temperature, max tokens)

## 🛠️ Technologies Used

- **Python 3.12+** (< 3.14)
- **Poetry** - Dependency management and packaging
- **Gradio 5.x** - Web UI framework for ML applications
- **LangChain** - LLM application framework
- **LangChain-IBM** - IBM Watsonx integration for LangChain
- **IBM Watsonx AI** - Enterprise AI platform
- **ChromaDB** - Vector database for embeddings
- **PyPDF** - PDF processing capabilities
- **python-dotenv** - Environment variable management

## 📦 Installation

### Prerequisites
- Python 3.12 or 3.13
- Poetry (install from [python-poetry.org](https://python-poetry.org/docs/#installation))

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
   poetry run python LLM/simple_gradio_llm.py
   ```

4. **Set up environment variables**
   
   Create a `.env` file in the `LLM/` directory:
   ```env
   WATSONX_API_KEY=your_api_key_here
   ```

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

### Running the Q&A Chatbot

**CLI Version:**
```bash
poetry run python LLM/simple_llm.py
```

**Gradio Web Interface:**
```bash
poetry run python LLM/simple_gradio_llm.py
```

Then open your browser and navigate to: `http://127.0.0.1:8080`

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

The LLM is configured with the following parameters in `simple_gradio_llm.py`:

```python
model_id = 'ibm/granite-3-3-8b-instruct'
parameters = {
    GenParams.MAX_NEW_TOKENS: 256,
    GenParams.TEMPERATURE: 0.5,
}
```

You can adjust these parameters to modify the chatbot's behavior:
- `MAX_NEW_TOKENS`: Maximum length of generated responses (default: 256)
- `TEMPERATURE`: Controls randomness (0.0 = deterministic, 1.0 = creative)

## 📚 Learning Highlights

### Gradio Input Types Explored
- ✅ Number inputs
- ✅ Textbox (single & multi-line)
- ✅ Slider
- ✅ Dropdown (single & multi-select)
- ✅ Checkbox & CheckboxGroup
- ✅ Radio buttons

### Key Concepts Learned
1. Creating simple Gradio interfaces with `gr.Interface()`
2. Handling multiple input/output types
3. Using examples for better UX
4. Integrating external APIs (IBM Watsonx)
5. Managing environment variables securely
6. Building conversational AI interfaces

## 🔒 Security Notes

- API keys are stored in `.env` files (excluded from version control)
- Never commit sensitive credentials to the repository
- The `.gitignore` file properly excludes secrets and environment files

## 🚧 Future Improvements

- [ ] Add conversation history/memory
- [ ] Implement streaming responses
- [ ] Add more LLM models support
- [ ] Deploy to cloud platform
- [ ] Leverage ChromaDB for RAG (Retrieval Augmented Generation)
- [ ] Implement PDF document processing with PyPDF
- [ ] Add vector search capabilities

## 📖 Resources

- [Gradio Documentation](https://www.gradio.app/docs)
- [LangChain Documentation](https://python.langchain.com/)
- [IBM Watsonx AI Documentation](https://www.ibm.com/docs/en/watsonx-as-a-service)

## 👨‍💻 Author

Learning and building practical AI applications with Gradio and IBM Watsonx AI.

## 📝 License

This is a learning project. Feel free to use and modify as needed for educational purposes.

---

**Note:** This project requires an IBM Watsonx AI account and API key. Visit [IBM Watsonx](https://www.ibm.com/watsonx) to get started.