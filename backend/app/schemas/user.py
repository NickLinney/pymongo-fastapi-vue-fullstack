from pydantic import BaseModel

class UserBase(BaseModel):
    name: str
    email: str

class UserCreate(UserBase):
    hashed_password: str

class User(UserBase):
    id: str

    class Config:
        orm_mode = True
