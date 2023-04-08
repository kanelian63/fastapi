from pydantic import BaseModel
from typing import List

class Event(BaseModel):
    id: int
    title: str
    image: str
    description: str
    tags: List[str]
    location: str

    class Config:
        schema_extra = {
            "example": {
                "title": "FastAPI Book Launch",
                "image": "https://linktomyimage.com/image.png",
                "description": "we will be discussing the contens of the FastAPI book in this event.",
                "tags": ["python", "fastapi", "book", "launch"],
                "location": "google meet"
            }
        }