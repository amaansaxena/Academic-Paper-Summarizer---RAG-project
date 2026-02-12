Here’s a **detailed but simple README** you can paste directly into your project.

---

# 📄 Research Paper Analyst (Local RAG App)

A simple local **Research Paper Question-Answering app** built with **Streamlit + LlamaIndex + Groq**.
Upload a research paper PDF and ask questions about it. The app reads the paper, creates embeddings, and lets you chat with it.

This project is intentionally **simple, beginner-friendly, and runs locally**.

---

## 🚀 What this project does

* Upload a research paper (PDF)
* Automatically reads and indexes the document
* Generates a short summary
* Lets you ask questions about the paper
* Answers based only on the uploaded PDF

This is a basic **RAG (Retrieval Augmented Generation)** setup.

---

## 🧠 How it works (simple explanation)

1. You upload a PDF
2. The app reads the text from the paper
3. It converts text into embeddings
4. Stores them in a vector index
5. When you ask a question:

   * It finds relevant parts of the paper
   * Sends them to the LLM
   * Returns an answer

Everything runs locally except the LLM call (Groq API).

---

## 🛠 Tech stack

* **Python**
* **Streamlit** – UI
* **LlamaIndex** – RAG pipeline
* **Groq API** – LLM
* **HuggingFace embeddings**
* **dotenv** – environment variables

---

## 📦 Installation

### 1. Clone repo

```bash
git clone <your-repo-link>
cd research-rag
```

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate   # mac/linux
venv\Scripts\activate      # windows
```

### 3. Install requirements

```bash
pip install -r requirements.txt
```

If no requirements file:

```bash
pip install streamlit llama-index llama-index-llms-groq llama-index-embeddings-huggingface python-dotenv
```

---

## 🔑 Setup API key

Create a `.env` file in the root folder:

```
GROQ_API_KEY=your_key_here
```

Get key from:
[https://console.groq.com](https://console.groq.com)

---

## ▶️ Run the app locally

```bash
streamlit run app.py
```

Then open in browser:

```
http://localhost:8501
```

This app is designed to run **locally on your machine**.
No deployment required.

---

## 📂 Project structure

```
project/
│
├── app.py
├── .env
├── requirements.txt
└── README.md
```

Temporary uploaded PDFs are stored locally while running.

---

## 💬 Features

* Upload research PDFs
* Auto summary
* Ask questions
* Chat style interface
* Uses embeddings for accurate answers
* Simple UI
* Runs locally

---

## ⚠️ Limitations

* Single PDF at a time
* No database storage
* Not optimized for huge papers
* Basic RAG only
* Requires internet for LLM

This project is meant for **learning and demonstration**, not production.

---

## 🎯 Why this project exists

This is a **simple RAG demo** to understand:

* Document indexing
* Embeddings
* Vector search
* LLM question answering
* Streamlit apps

The goal was to keep everything **easy to understand and run locally**.

---

## 🔮 Possible improvements

* Multiple PDFs
* Citations with page numbers
* Chat memory
* Highlight text in PDF
* Better UI
* Deployment
* Database storage

---

## 👨‍💻 Author note

This project is intentionally kept **simple and readable**.
It is designed for students or beginners learning RAG systems.

Runs locally.
Minimal setup.
Easy to understand code.

---

## 📜 License

Free to use for learning and educational purposes.
