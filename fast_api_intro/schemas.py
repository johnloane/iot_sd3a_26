from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, EmailStr


class UserBase(BaseModel):
    username: str = Field(min_length=1, max_length=50)
    email: EmailStr = Field(max_length=255)
    
class UserCreate(UserBase):
    pass 

class UserResponse(UserBase):
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    image_file: str | None
    image_path: str

class ReadingBase(BaseModel):
    sensor : str = Field(min_length=1, max_length=20)
    content : float
    
    
class ReadingCreate(ReadingBase):
    user_id: int 

class ReadingResponse(ReadingBase):
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    user_id: int
    date_timestamp_posted: datetime
    author: UserResponse
    
    
    
    
