from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from src.services.emotion_analyzer import analyze_text_with_gemini, process_emotions_response

router = APIRouter()

class EmotionRequest(BaseModel):
    text: str

@router.post("/analyze")  # Changed from /analyze-emotions to /analyze
async def analyze_emotions(request: EmotionRequest):
    if not request.text:
        raise HTTPException(status_code=400, detail="Text input cannot be empty.")
    
    try:
        response = analyze_text_with_gemini(request.text)
        emotions = process_emotions_response(response)
        return emotions
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))