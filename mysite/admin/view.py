from db.models import UserProfile,Category,SubCategory,Product,Review
from sqladmin import ModelView


class UserProfileView(ModelView, model=UserProfile):
    column_list = [UserProfile.id,UserProfile.username,UserProfile.email]


class CategoryView(ModelView, model=Category):
    column_list = [Category.id,Category.category_name]

class SubCategoryView(ModelView, model=SubCategory):
    column_list = [SubCategory.id,SubCategory.sub_category_name]


class ProductView(ModelView,model=Product):
    column_list = [Product.id,Product.product_name]

class ReviewView(ModelView,model=Review):
    column_list = [Review.id,Review.user]












