from app.retrieval.vector_search import vector_search
from app.retrieval.graph_search import graph_search


def hybrid_search(query: str):

    vector_results = vector_search(query)

    # For now, we're using CUDA as the graph entity.
    # Later we'll automatically extract the entity from the user's question.
    graph_results = graph_search("CUDA")

    context = ""

    # Add vector search results
    for row in vector_results:
        context += row.chunk_text + "\n\n"

    # Add graph relationships
    for relation in graph_results:
        context += (
            f"{relation['source']} "
            f"{relation['relation']} "
            f"{relation['target']}\n"
        )

    return context