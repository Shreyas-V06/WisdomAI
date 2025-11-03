import os
from dotenv import load_dotenv
import google.generativeai as genai 
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
import os
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
from google import genai
from google.genai import types
import base64
import os

load_dotenv()

def initialize_processor_llm():
    GeminiApiKey=os.getenv('GOOGLE_API_KEY')
    genai.configure(api_key=GeminiApiKey)
    GeminiLLM = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
    return GeminiLLM

def invoke_conversation_processor(conversation:str):
    client = genai.Client(
    vertexai=True,
    project="104610138887",
    location="us-central1"
    )

    prompt=f"""You are an AI model that organizes multi-person chat conversations into structured topic-based summaries.
For the given chat conversation, group messages into clear, self-contained topics.Each topic should include: Topic, summary, outcome and end it with the delimiter ###END OF TOPIC### ( case sensitive )
CHAT CONVERSATION:

{conversation}
"""
    model = "projects/104610138887/locations/us-central1/models/7593006299583873024"
    model_endpoint = "projects/104610138887/locations/us-central1/endpoints/2497570349307133952"
    contents = [
    types.Content(
        role="user",
        parts=[types.Part.from_text(text=prompt)]
    )
    ]

    response = client.models.generate_content(
    model=model_endpoint,
    contents=contents,
    config=types.GenerateContentConfig(
        temperature=0.3,
        max_output_tokens=256,
    ),
    )
    answer = response.text
    return answer

def initialize_chat_llm():
    llm = ChatGroq(model="llama-3.3-70b-versatile")
    return llm


