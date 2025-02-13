from fastapi import FastAPI
from app.core.routing import api_router
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
import uvicorn

app = FastAPI()

app.include_router(api_router)

# QA_Agent_Application = FastAPI(
#     title="QA_Agent",    
#     version="0.2.1",
#      swagger_ui_parameters={"defaultModelsExpandDepth": -1, "displayRequestDuration": True,
#         "tryItOutEnabled": True,},
# )

# QA_Agent_Application.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# QA_Agent_Application.add_middleware(SessionMiddleware, secret_key="My_Agent")
# QA_Agent_Application.include_router(api_router, prefix="/v1")

# # Include API routes
# app.include_router(api_router)

# if __name__ == "__main__":
#     uvicorn.run("app.main:QA_Agent_Application", host="0.0.0.0", port=5000, reload=True)