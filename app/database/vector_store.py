from sqlalchemy import text
from app.core.database import engine


def insert_document(chunk_text: str, embedding):
    """
    Store a document chunk and its embedding in PostgreSQL.
    """

    embedding_list = embedding.tolist()

    with engine.begin() as conn:
        conn.execute(
            text("""
                INSERT INTO documents (chunk_text, embedding)
                VALUES (:chunk_text, :embedding)
            """),
            {
                "chunk_text": chunk_text,
                "embedding": embedding_list,
            },
        )