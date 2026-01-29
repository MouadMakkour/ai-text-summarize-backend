from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.summarize import router as summarize_router

app = FastAPI(title="AI Text Summarizer API")

origins = [
    "https://ai-text-summarize-frontend-bolf6y7n1-mouad-makkours-projects.vercel.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(summarize_router)

@app.get("/")
def health_check():
    return {"status": "ok"}