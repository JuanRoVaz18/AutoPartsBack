from pydantic import BaseModel

class ImageBase(BaseModel):
    name: str
    url: str

class ImageCreate(ImageBase):
    pass

class ImageUpdate(BaseModel):
    name: str | None = None
    url: str | None = None

class Image(ImageBase):
    id: int

    model_config = {"from_attributes": True}
