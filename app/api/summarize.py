from fastapi import APIRouter, HTTPException
from app.schemas.summarize import SummarizeRequest, SummarizeResponse
from app.services.ai_service import summarize_text

router = APIRouter(prefix="/summarize", tags=["Summarize"])

@router.post("", response_model=SummarizeResponse)
def summarize(request: SummarizeRequest):
    if not request.text.strip():
        raise HTTPException(status_code=400, detail="Text cannot be empty")

    summary = summarize_text(request.text)
    return SummarizeResponse(summary=summary)