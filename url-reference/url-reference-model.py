from pydantic import BaseModel

class UrlReferenceModel:
    url_target: str
    url_reference: str