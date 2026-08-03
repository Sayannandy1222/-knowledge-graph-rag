from app.ingestion.loader import load_pdf
from app.ingestion.splitter import split_text

text = load_pdf("data/sample.pdf")

chunks = split_text(text)

print("=" * 80)
print(f"Total Chunks : {len(chunks)}")
print("=" * 80)

print("\nFirst Chunk:\n")
print(chunks[0])

print("\n" + "=" * 80)

print(f"First Chunk Length : {len(chunks[0])}")