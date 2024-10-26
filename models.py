from pydantic import BaseModel, Field, EmailStr
from typing import List, Optional

class Participante(BaseModel):
    id: str = Field(..., example='p1')
    name: str = Field(..., example='Juan')
    email: EmailStr = Field(..., example='juan.perez@example.com')
    registration_date: str = Field(..., example='2024-10-23T19:00:00Z')


class Evento(BaseModel):
    id: str = Field(..., example='e1')
    name: str = Field(..., example='Conferencia TEC 2024')
    description: Optional[str] = Field(None, example='Una Conferencia sobre las ultimas tendencias en tecnologia')
    date: str = Field(..., example='2024-10-23T19:00:00Z')
    location: str = Field(..., example='Centro de convenciones Ciudad')
    capacity: int = Field(..., ge=1, example = 300)
    participants: List[Participante] = Field(default_factory=list)