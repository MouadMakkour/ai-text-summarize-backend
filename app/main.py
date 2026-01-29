from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.summarize import router as summarize_router

app = FastAPI(title="AI Text Summarizer API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for demo !!
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(summarize_router)

@app.get("/")
def health_check():
    return {"status": "ok"}