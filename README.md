# 📘 PDF Q&A App (RAG with LlamaIndex + Groq)

This is a Streamlit-based application that allows users to upload a PDF and ask questions about its content using Retrieval-Augmented Generation (RAG). The app leverages LlamaIndex for document indexing, HuggingFace embeddings for semantic search, and Groq's blazing-fast LLaMA3 model for generating detailed answers.

---

## 🔗 Live App

🌐 [Click here to use the app](https://your-username-your-repo-name.streamlit.app)

---

## 🧠 How It Works

1. **Upload a PDF** file.
2. The document is split into chunks using a sentence-level splitter.
3. Embeddings are generated using a HuggingFace model.
4. Chunks are indexed using `VectorStoreIndex` from LlamaIndex.
5. Questions are enhanced for clarity.
6. The index is queried using a retriever and LLaMA3 via Groq to generate answers.

---

## 🛠 Tech Stack

| Component         | Technology                             |
|------------------|----------------------------------------|
| UI               | Streamlit                              |
| Embedding Model  | HuggingFace (`all-MiniLM-L6-v2`)       |
| LLM              | Groq API (`llama3-70b-8192`)           |
| Vector Store     | LlamaIndex `VectorStoreIndex`          |
| Query Engine     | `RetrieverQueryEngine`                 |

---

## 📦 Installation

```bash
git clone https://github.com/your-username/pdf-qa-app.git
cd pdf-qa-app
pip install -r requirements.txt
```
---
## 🔐 Environment Setup
Create a .streamlit/secrets.toml file for your API keys:

```bash
MODEL_NAME = "llama3-70b-8192"
GROQ_API_KEY = "your_groq_api_key_here"
```
---
## 📁 Folder Structure
```
pdf_qa_app/
├── main.py               # Streamlit app
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
└── .streamlit/
    └── secrets.toml      # Groq credentials (DO NOT UPLOAD)
```
---
## 📷 App Preview
Upload a document → Ask a question → Get an accurate, LLM-generated answer with context from your PDF.

---
## 💡 Example Use Cases
Academic paper Q&A

Company reports summarization

Legal document understanding

PDF-based chatbots


---
## 📜 License
This project is licensed under the MIT License.


---
## 🙌 Acknowledgements
LlamaIndex

Groq

Streamlit

HuggingFace Transformers

---
