from pydantic import BaseModel

class GenerateLinkDto(BaseModel):
    url_target: str