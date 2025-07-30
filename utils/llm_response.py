import os
from dotenv import load_dotenv
from google import genai
from google.genai.types import GenerateContentConfig

from concurrent.futures import ThreadPoolExecutor

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY")) 

SYSTEM_INSTRUCTION = [
    "You are an intelligent insurance parser.",
    "Answer insurance-related questions professionally and concisely.",
    "Use relevant clauses for answers but do NOT reference clause numbers or sources.",
    "Respond in one line using a professional tone.",
    "Format your response in Markdown."
]

MODEL_ID = "gemini-2.5-flash"

def generate_structured_output(query, clauses):
    context = "\n\n".join([
        f"[Clause from {doc.metadata.get('source', 'unknown')}]:\n{doc.page_content}"
        for doc in clauses
    ])

    chat = client.chats.create(
        model=MODEL_ID,
        config=GenerateContentConfig(
            system_instruction=SYSTEM_INSTRUCTION,
            temperature=0.2,
        ),
    )
    
    full_prompt = f"Context:\n{context}\n\nQuestion:\n{query}"

    try:
        response = chat.send_message(full_prompt)

        return response.text.strip()
    except Exception as e:
        return f"Error generating response for '{query}': {str(e)}"


def generate_structured_answers(questions, vectorstore):
    from utils.retriever import get_relevant_clauses

    def process(q):
        clauses = get_relevant_clauses(q, vectorstore)
        return generate_structured_output(q, clauses)

    with ThreadPoolExecutor() as executor:
        answers = list(executor.map(process, questions))

    return answers