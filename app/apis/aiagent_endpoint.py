from fastapi import APIRouter, Request, HTTPException
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from app.schema.models import Message
import os
from dotenv import load_dotenv

router = APIRouter()

import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
print(f"Loaded API Key: {OPENAI_API_KEY[:5]}... (masked for security)")


memory = ConversationBufferMemory()

def get_conversation_history():
    return memory.load_memory_variables({})["history"]

@router.post("/chat")
async def chat(request: Request, input_message: Message):
    user_input = input_message.message.strip()
    try:

        response_data = {
            "response_content": "",
        }

        conversation_history = get_conversation_history()

        prompt = f"""Hi there! 👋 I'm here to help with any questions you have. Feel free to ask away!

            Role: Friendly Customer Support Chatbot
            Tone: Simple, approachable, and cheerful

            Instructions:

            Analyze the user's input: {user_input}
            Review conversation history (if relevant): {conversation_history}
            
            Provide a clear, concise answer that addresses all parts of the query.
            Keep responses conversational (avoid jargon).
            Use the conversation history to maintain context (e.g., follow-ups, past issues).
            End with a follow up question.

            """
        
        llm = ChatOpenAI(model_name="gpt-4", openai_api_key=OPENAI_API_KEY)
        response = llm.invoke([{"role": "user", "content": prompt}])
        response_data['response_content'] = response.content.lower()

        memory.save_context({"input": user_input}, {"output": response_data['response_content']})
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing chatbot response: {str(e)}")

    return response_data