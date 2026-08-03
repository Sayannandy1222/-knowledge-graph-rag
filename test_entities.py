from app.ingestion.loader import load_pdf
from app.ingestion.splitter import split_text

from app.graph.entity_extractor import extract_entities
from app.graph.neo4j_store import create_entity

text = load_pdf("data/sample.pdf")
chunks = split_text(text)

entities = extract_entities(chunks[0])

print("\nEntities Found:\n")

for entity in entities:
    print("-", entity)
    create_entity(entity)

print("\n✅ All entities inserted into Neo4j!")