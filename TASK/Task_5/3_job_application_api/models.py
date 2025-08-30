from pydantic import BaseModel

class JobApplication(BaseModel):
    name: str
    company: str
    position: str
    status: str  # pending, accepted, rejected