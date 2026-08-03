from app.ingestion.embeddings import generate_embeddings
from app.retrieval.search import search_similar

query = "Explain CUDA Memory Hierarchy"

print(f"\nQuery: {query}\n")

# Generate embedding for the query
query_embedding = generate_embeddings([query])[0]

# Search PostgreSQL
results = search_similar(query_embedding)

print("=" * 80)

for row in results:
    print(f"\nDocument ID : {row.id}")
    print(f"Distance    : {row.distance:.4f}")
    print("-" * 80)
    print(row.chunk_text[:500])
    print("=" * 80)