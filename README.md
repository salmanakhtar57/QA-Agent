# FastAPI Chatbot

This project is a chatbot built using FastAPI and LangChain, leveraging OpenAI's GPT model for conversational AI. The chatbot maintains context using a conversation buffer memory and provides friendly, concise, and helpful responses.

## Features
- FastAPI-based backend
- OpenAI gpt-4o-mini integration
- Conversation history management using LangChain memory
- API endpoint for chatbot interaction
- Simple and friendly chatbot responses
- Supports follow-up questions while maintaining context

## Installation

### 1. Clone the repository

git clone https://github.com/<your-repo-name>.git
cd <your-repo-name>

### Create a virtual environment
1. python -m venv venv
### Activate virstual environemtn 
source venv/bin/activate Or on Windows use `venv\Scripts\activate`

### Install Dependencies

pip install -r requirements.txt

### Set up environment variables:

create a .env file and add:

OPENAI_API_KEY=your-openai-api-key

## Running the Project

### Start the FastAPI server:

uvicorn app.main --reload

### Access API documentation:

    Swagger UI: http://127.0.0.1:8000/docs
    Redoc: http://127.0.0.1:8000/redoc


## API Endpoints

### Chat Endpoint

    URL: /ai_agent/chat
    Method: POST
    Request Body:

{
  "message": "Your question here"
}

Response:

{
  "response_content": "Chatbot's response"
}

## Contributing

Feel free to open issues or submit pull requests for improvements.