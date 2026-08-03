from app.ingestion.loader import load_pdf
from app.ingestion.splitter import split_text
from app.ingestion.embeddings import generate_embeddings

text = load_pdf("data/sample.pdf")
chunks = split_text(text)

# Test only the first 5 chunks for now
embeddings = generate_embeddings(chunks[:5])

print("=" * 80)
print(f"Chunks: {len(chunks[:5])}")
print(f"Embeddings: {len(embeddings)}")
print(f"Embedding Dimension: {len(embeddings[0])}")
print("=" * 80)

print("\nFirst 10 values of the first embedding:\n")
print(embeddings[0][:10])