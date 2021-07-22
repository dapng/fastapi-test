from pydantic import BaseModel, validator, Field
from datetime import date
from typing import List

class Genre(BaseModel):
    name: str

class Author(BaseModel):
    first_name: str
    last_name: str
    age: int = Field(..., gt=15, lt=90, description="Возраст не меньше 15 и не более 90 лет")

    # @validator('age')
    # def check_age(cls, v):
    #     if v < 15:
    #         raise ValueError('Автор не может быть меньше 15')
    #     return v

class Book(BaseModel):
    title: str
    writer: str
    duration: str
    date: date
    summary: str
    genres: List[Genre] = []
    pages: int

class BookOut(Book):
    id: int
