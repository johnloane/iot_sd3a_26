from pydantic import BaseModel, ConfigDict, Field

class ReadingBase(BaseModel):
    sensor : str = Field(min_length=1, max_length=20)
    content : float
