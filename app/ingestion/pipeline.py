from app.ingestion.loader import load_pdf
from app.ingestion.splitter import split_text
from app.ingestion.embeddings import generate_embeddings

from app.database.vector_store import insert_document

from app.graph.entity_extractor import extract_entities
from app.graph.relation_extractor import extract_relationships
from app.graph.neo4j_store import (
    insert_entities,
    insert_relationships,
)


def ingest_pdf(file_path: str):
    """
    Complete ingestion pipeline.
    """

    # Load PDF
    text = load_pdf(file_path)

    # Split document into chunks
    chunks = split_text(text)

    # Generate embeddings
    embeddings = generate_embeddings(chunks)

    # Store vectors in PostgreSQL
    for chunk, embedding in zip(chunks, embeddings):
        insert_document(chunk, embedding)

    # ------------------------------------------
    # Build Knowledge Graph (Chunk by Chunk)
    # ------------------------------------------

    all_entities = set()
    all_relationships = []

    for chunk in chunks:

        # Extract entities
        entities = extract_entities(chunk)
        all_entities.update(entities)

        # Extract relationships
        relationships = extract_relationships(chunk)
        all_relationships.extend(relationships)

    # Store in Neo4j
    insert_entities(list(all_entities))
    insert_relationships(all_relationships)

    return {
        "chunk_count": len(chunks),
        "entity_count": len(all_entities),
        "relationship_count": len(all_relationships),
    }