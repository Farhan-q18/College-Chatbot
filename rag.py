from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
import os

load_dotenv()

# Create embeddings
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Load or create DB (IMPORTANT OPTIMIZATION)
if not os.path.exists("chroma-db"):
    print("🔄 Creating vector database...")

    loader = PyPDFLoader("document_loaders/BTech_2025_2026.pdf")
    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    chunks = splitter.split_documents(docs)

    db = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory="chroma-db"
    )
    db.persist()

    print("✅ Database created!\n")

else:
    print("⚡ Loading existing database...\n")
    db = Chroma(
        persist_directory="chroma-db",
        embedding_function=embedding_model
    )

# Search function
def search_pdf(query):
    results = db.similarity_search(query, k=2)

    if results:
        return f"📄 According to the document:\n\n{results[0].page_content}"
    else:
        return "❌ Sorry, I couldn't find relevant information."

# 🔥 Interactive loop
if __name__ == "__main__":
    print("🤖 PDF Chatbot Ready! Type 'exit' to stop.\n")

    while True:
        query = input("You: ")

        if query.lower() in ["exit", "quit", "bye"]:
            print("Bot: Goodbye! 👋")
            break

        response = search_pdf(query)
        print(f"Bot: {response}\n")