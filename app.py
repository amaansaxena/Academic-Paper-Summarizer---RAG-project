import os
import streamlit as st
from dotenv import load_dotenv

from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.llms.groq import Groq
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

# ---------- Load API key ----------
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    st.error("GROQ_API_KEY not found in .env file")
    st.stop()

# ---------- Page config ----------
st.set_page_config(
    page_title="Research Paper Analyst",
    page_icon="📄",
    layout="wide"
)

# ---------- Sidebar ----------
st.sidebar.title("📄 Research RAG")
st.sidebar.success(f"API key loaded: {api_key[:5]}***")
st.sidebar.markdown("Upload a research paper and ask questions about it.")

# ---------- Title ----------
st.title("📄 Research Paper Analyst")
st.caption("Upload a research paper and chat with it")

# ---------- Model setup ----------
Settings.llm = Groq(
    model="llama-3.3-70b-versatile",
    api_key=api_key
)

Settings.embed_model = HuggingFaceEmbedding(
    model_name="BAAI/bge-small-en-v1.5"
)

# ---------- Session state ----------
if "index" not in st.session_state:
    st.session_state.index = None

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ---------- Upload section ----------
st.subheader("Upload Paper")

uploaded_file = st.file_uploader(
    "Upload a PDF",
    type="pdf",
    label_visibility="collapsed"
)

if uploaded_file:
    temp_path = "temp_paper.pdf"
    with open(temp_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    with st.spinner("Reading paper..."):
        try:
            docs = SimpleDirectoryReader(input_files=[temp_path]).load_data()
            st.session_state.index = VectorStoreIndex.from_documents(docs)

            query_engine = st.session_state.index.as_query_engine()

            summary = query_engine.query(
                "Give a short summary with objective, method, and key results."
            )

            st.success("Paper processed successfully")

            with st.expander("📑 Paper Summary", expanded=True):
                st.write(str(summary))

        except Exception as e:
            st.error(f"Error: {e}")

# ---------- Chat section ----------
if st.session_state.index:
    st.divider()
    st.subheader("Ask questions")

    user_query = st.chat_input("Ask something about the paper...")

    if user_query:
        st.session_state.chat_history.append(("user", user_query))

        with st.spinner("Thinking..."):
            query_engine = st.session_state.index.as_query_engine()
            response = query_engine.query(user_query)
            answer = str(response)

        st.session_state.chat_history.append(("bot", answer))

    # display chat
    for role, msg in st.session_state.chat_history:
        if role == "user":
            st.chat_message("user").write(msg)
        else:
            st.chat_message("assistant").write(msg)
