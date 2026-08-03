from app.retrieval.hybrid_search import hybrid_search
from app.llm.rag import generate_answer

question = "Explain CUDA."

print("\nBuilding Hybrid Context...\n")

context = hybrid_search(question)

print("\nGenerating AI Answer...\n")

answer = generate_answer(question, context)

print("=" * 80)
print("AI ANSWER")
print("=" * 80)
print(answer)