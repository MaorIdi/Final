from pydantic import BaseModel

class VirtualMachine(BaseModel):
    name: str
    cpu: float
    memory: float
    disk: float