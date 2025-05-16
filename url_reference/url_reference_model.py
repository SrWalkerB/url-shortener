import uuid
from sqlmodel import SQLModel, Field

class UrlReferenceModel(SQLModel, table=True):
    __tablename__ = 'url_reference'

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    url_target: str
    url_code: str


    