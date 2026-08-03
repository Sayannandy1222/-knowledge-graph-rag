from app.ingestion.loader import load_pdf
from app.ingestion.splitter import split_text
from app.ingestion.embeddings import generate_embeddings
from app.database.vector_store import insert_document

print("Loading PDF...")
text = load_pdf("data/sample.pdf")

print("Splitting into chunks...")
chunks = split_text(text)

print("Generating embeddings...")
embeddings = generate_embeddings(chunks[:5])

print("Inserting into PostgreSQL...")

for chunk, embedding in zip(chunks[:5], embeddings):
    insert_document(chunk, embedding)

print("✅ Successfully inserted 5 document chunks into PostgreSQL!")