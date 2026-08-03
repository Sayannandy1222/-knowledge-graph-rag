from sentence_transformers import SentenceTransformer

# Load the model only once
model = SentenceTransformer("BAAI/bge-small-en-v1.5")


def generate_embeddings(chunks):
    """
    Generate embeddings for a list of text chunks.
    """
    embeddings = model.encode(
        chunks,
        convert_to_numpy=True,
        show_progress_bar=True,
    )

    return embeddings