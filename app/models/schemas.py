from pydantic import BaseModel


class URLInput(BaseModel):
    url: str


class ModelResponse(BaseModel):
    url: str
    classification: str
