from pydantic import BaseModel,EmailStr
from typing import Optional

class RegisterSchema(BaseModel):
     first_name:str | None
     last_name:str | None
     username:str
     phone_number:str
     email:EmailStr
     password:str

class LoginSchema(BaseModel):
    username: str
    password:str

class UserProfileUpdateSchema(BaseModel):
    first_name:Optional[str]
    last_name:str | None
    username:str
    age:int | None
    phone_number:str
    profile_image:Optional[str]
    email:EmailStr

class UserProfileListSchema(BaseModel):
    username:str
    phone_number:str
    profile_image:Optional[str]

class UserProfileDetailSchema(BaseModel):
    first_name:str
    last_name:str
    username:str
    age:int | None
    phone_number:str
    profile_image:Optional[str]


class CategoryCreateSchema(BaseModel):
    category_name:str
    category_image:str

class CategoryListSchema(BaseModel):
    id:int
    category_name:str
    category_image:str

class SubCategorySchema(BaseModel):
    category_id:int
    sub_category_name:str

class ProductCreateSchema(BaseModel):
    category_id:int
    sub_category_name:int
    product_name:str
    product_image:str
    price:int
    owner_id:int
    description:str | None

class ProductListSchema(BaseModel):
    category_id:int
    sub_category_name:int
    product_name:str
    product_image:str

class ProductDetailSchema(BaseModel):
    category_id:int
    sub_category_name:int
    product_name:str
    product_image:str
    price:int
    owner_id:int
    description:str | None


class ImageProductSchema(BaseModel):
    product_id:int
    image:str

class ReviewCreateSchema(BaseModel):
    user_id:int
    product_id:int
    comment:str | None
    stars:int | None
    image:Optional[str]
    video:Optional[str]

class ReviewListSchema(BaseModel):
    user_id:int
    product_id:int
    comment:str | None
    stars:int | None


class CartSchema(BaseModel):
    user_id:int


class CartItemSchema(BaseModel):
    cart_id:int
    product_id:int


class FavoriteSchema(BaseModel):
    user_id:int
    product_id:int
    like:bool













