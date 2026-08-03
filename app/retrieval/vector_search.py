from sentence_transformers import SentenceTransformer
from sqlalchemy import text

from app.core.database import engine

model = SentenceTransformer("BAAI/bge-small-en-v1.5")


def vector_search(query: str, limit: int = 3):
    embedding = model.encode(query).tolist()

    sql = text("""
        SELECT
            id,
            chunk_text
        FROM documents
        ORDER BY embedding <=> CAST(:embedding AS vector)
        LIMIT :limit;
    """)

    with engine.connect() as conn:
        rows = conn.execute(
            sql,
            {
                "embedding": str(embedding),
                "limit": limit,
            },
        ).fetchall()

    return rows