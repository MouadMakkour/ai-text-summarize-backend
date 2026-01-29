from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.summarize import router as summarize_router

app = FastAPI(title="AI Text Summarizer API")

# CORS middleware 
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://ai-text-summarize-frontend-bolf6y7n1-mouad-makkours-projects.vercel.app",
        "https://*.vercel.app",
    ],
    allow_credentials=False,
    allow_methods=["GET", "POST", "OPTIONS", "HEAD"],
    allow_headers=["*"],
    expose_headers=["*"],
)

# Include the summarize router
app.include_router(summarize_router, prefix="/summarize")

# Health check endpoint - support both GET and HEAD
@app.get("/")
@app.head("/")
def health_check():
    return {"status": "ok"}