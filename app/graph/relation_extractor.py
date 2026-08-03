import json

from groq import Groq

from app.core.config import settings

client = Groq(api_key=settings.GROQ_API_KEY)


def extract_relationships(text: str):

    prompt = f"""
You are an AI Knowledge Graph builder.

Extract relationships from the following text.

Return ONLY valid JSON.

Example:

[
    {{
        "source":"CUDA",
        "relation":"USES",
        "target":"GPU"
    }},
    {{
        "source":"CUDA",
        "relation":"SUPPORTS",
        "target":"Thread Hierarchy"
    }}
]

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

    content = response.choices[0].message.content

    return json.loads(content)