from pydantic import EmailStr ,BaseModel #specificaly used for data validation and settings management using Python type annotations. It allows you to define data models with type hints, and it will automatically validate the data against those models.
from datetime import datetime
from typing import Optional
from pydantic import conint # it is used for validating that the value is an integer and it is greater than or equal to a certain value. In this case, we will use it to validate that the dir value is either 0 or 1.

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

class UserOut(BaseModel):
    id:int
    email: EmailStr
    created_at: datetime
    class Config:
        orm_mode= True


class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut
    class Config:
        orm_mode = True # it tells pydantic to read the data even if it is not a dict, but an ORM model. It will convert the ORM model to a dict and then validate the data against the Post model.


class PostOut(BaseModel):
    post: Post
    votes: int

    class Config:
        orm_mode = True
    

class UserCreate(BaseModel):
    email: EmailStr
    password: str



class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: int | None = None



class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)