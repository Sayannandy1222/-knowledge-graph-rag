from groq import Groq
from app.core.config import settings

client = Groq(api_key=settings.GROQ_API_KEY)


def extract_entities(text: str):
    prompt = f"""
You are an AI Knowledge Graph extractor.

Extract only important technical entities.

Return ONLY a comma separated list.

Text:

{text}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        temperature=0,
    )

    entities = response.choices[0].message.content

    return [
        entity.strip()
        for entity in entities.split(",")
        if entity.strip()
    ]