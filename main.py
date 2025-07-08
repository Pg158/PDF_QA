import streamlit as st
import os
import tempfile
import hashlib
from dotenv import load_dotenv
from llama_index.core import SimpleDirectoryReader, Settings
from llama_index.core.node_parser import SentenceSplitter
from llama_index.embeddings import HuggingFaceEmbedding
from llama_index.core import VectorStoreIndex
from llama_index.llms.groq import Groq
from llama_index.core.query_engine import RetrieverQueryEngine

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
model_name =os.getenv("MODEL_NAME")

st.set_page_config(page_title="PDF Q&A", layout="centered")
st.title("PDF Q&A Application")

embed_model = HuggingFaceEmbedding(model_name="sentence-transformers/all-MiniLM-L6-v2")
Settings.embed_model = embed_model
llm = Groq(model=model_name)
Settings.llm = llm

uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

def compute_file_hash(file_bytes: bytes) -> str:
    return hashlib.md5(file_bytes).hexdigest()
@st.cache_resource
def create_index_from_document(file_hash: str, file_bytes: bytes):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(file_bytes)
        tmp_file_path = tmp_file.name

    documents = SimpleDirectoryReader(input_files=[tmp_file_path]).load_data()
    splitter = SentenceSplitter(chunk_size=256)
    nodes = splitter.get_nodes_from_documents(documents)
    index = VectorStoreIndex(nodes)
    return index, documents, nodes

if uploaded_file is not None:
    file_bytes = uploaded_file.read()
    file_hash = compute_file_hash(file_bytes)

    index, documents, nodes = create_index_from_document(file_hash, file_bytes)

    st.subheader("Document Preview")
    st.write("Total documents loaded:", len(documents))
    st.write("First document length:", len(documents[0].text))
    st.write("Total chunks created:", len(nodes))

    def enhance_query(raw_query: str) -> str:
        system_prompt = (
            "You are a helpful assistant that rewrites vague or short questions into "
            "clear and complete ones for querying a document. ONLY rewrite, do not answer."
        )
        full_prompt = f"{system_prompt}\nOriginal: {raw_query}\nRewritten:"
        response = llm.complete(prompt=full_prompt)
        return response.text.strip()

    retriever = index.as_retriever(similarity_top_k=8)
    query_engine = RetrieverQueryEngine.from_args(retriever=retriever)
    user_query = st.text_input("Enter your question")

    if st.button("Submit") and user_query:
        st.write("Enhancing your query...")
        improved_query = enhance_query(user_query)
        st.write("Rewritten Query:", improved_query)

        st.write("Getting answer from the document...")
        response = query_engine.query(improved_query)
        st.write("Answer:")
        st.write(response.response)
