from app.ingestion.loader import load_pdf
from app.ingestion.splitter import split_text

from app.graph.entity_extractor import extract_entities
from app.graph.relation_extractor import extract_relationships
from app.graph.neo4j_store import (
    create_entity,
    create_ai_relationship,
)

text = load_pdf("data/sample.pdf")
chunks = split_text(text)

print("\nExtracting entities...")

entities = extract_entities(chunks[0])

for entity in entities:
    create_entity(entity)

print("Entities stored.")

print("\nExtracting relationships...")

relationships = extract_relationships(chunks[0])

for relation in relationships:

    create_ai_relationship(
        relation["source"],
        relation["relation"],
        relation["target"],
    )

print("\nKnowledge Graph Built Successfully!")