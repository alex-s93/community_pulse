from pydantic import BaseModel, Field


class QuestionCreate(BaseModel):
    text: str = Field(..., min_length=15)
    category_id: int = Field(...)


class QuestionResponse(BaseModel):
    id: int
    text: str
    category_id: int

    class Config:
        from_attributes = True


class CategoryCreateUpdate(BaseModel):
    name: str = Field(..., min_length=3, max_length=100)


class CategoryResponse(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True
