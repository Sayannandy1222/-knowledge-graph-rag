from app.ingestion.loader import load_pdf
from app.ingestion.splitter import split_text

from app.graph.relation_extractor import extract_relationships

text = load_pdf("data/sample.pdf")

chunks = split_text(text)

relationships = extract_relationships(chunks[0])

print()

print("Relationships Found:\n")

for relationship in relationships:
    print(relationship)