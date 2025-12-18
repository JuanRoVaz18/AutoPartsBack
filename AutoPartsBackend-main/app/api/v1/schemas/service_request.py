from pydantic import BaseModel

class ServiceRequestBase(BaseModel):
    description: str
    establishment_id: int

class ServiceRequestCreate(ServiceRequestBase):
    pass

class ServiceRequest(ServiceRequestBase):
    id: int

    class Config:
        orm_mode = True
