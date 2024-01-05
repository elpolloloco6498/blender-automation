from pydantic import BaseModel


class RenderSchema(BaseModel):
    text: str
