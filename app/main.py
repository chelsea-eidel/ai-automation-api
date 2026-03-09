from fastapi import FastAPI
from app.routes import router

app = FastAPI(
    title="AI Automation API",
    description="LLM-powered API for summarization, task extraction, and structured data conversion",
    version="0.1.0",
)

app.include_router(router)