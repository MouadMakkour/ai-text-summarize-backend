from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response  # Add this import
from app.api.summarize import router as summarize_router

app = FastAPI(title="AI Text Summarizer API")

# CORS middleware 
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://ai-text-summarize-frontend-bolf6y7n1-mouad-makkours-projects.vercel.app",
        "https://*.vercel.app",  # Allow all Vercel preview deployments
    ],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(summarize_router, prefix="/summarize")

@app.get("/")
def health_check():
    return {"status": "ok"}