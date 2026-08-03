from app.retrieval.vector_search import vector_search

results = vector_search("What is CUDA?")

print("\nSemantic Search Results\n")

for row in results:
    print("=" * 80)
    print(f"Document ID: {row.id}")
    print(row.chunk_text[:500])
    print()