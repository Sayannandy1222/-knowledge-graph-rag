from sqlalchemy import text
from app.core.database import engine


def search_similar(query_embedding, limit=5):
    """
    Search the most similar document chunks using pgvector.
    """

    with engine.connect() as conn:
        result = conn.execute(
            text("""
                SELECT
                    id,
                    chunk_text,
                    embedding <=> CAST(:embedding AS vector) AS distance
                FROM documents
                ORDER BY embedding <=> CAST(:embedding AS vector)
                LIMIT :limit;
            """),
            {
                "embedding": query_embedding.tolist(),
                "limit": limit,
            },
        )

        return result.fetchall()