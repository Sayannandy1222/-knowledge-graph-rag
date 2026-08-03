from app.ingestion.loader import load_pdf

text = load_pdf("data/sample.pdf")

print("=" * 80)
print(text[:1500])
print("=" * 80)
print(f"Total characters: {len(text):,}")