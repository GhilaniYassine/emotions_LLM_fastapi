
from pydantic import BaseModel
from typing import Dict

class EmotionResponse(BaseModel):
    emotions: Dict[str, str]