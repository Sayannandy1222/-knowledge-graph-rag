from app.retrieval.graph_search import graph_search

results = graph_search("CUDA")

print("\nGraph Search Results\n")

for result in results:
    print(result)