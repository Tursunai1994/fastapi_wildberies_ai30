
from fastapi import FastAPI
from api import user,category,sub_category,product,auth,review
import uvicorn
from admin.setup import setup_admin



wildberries_aap = FastAPI(title= 'FastAPI Wildberies ai30')
wildberries_aap.include_router(user.user_router)
wildberries_aap.include_router(category.category_router)
wildberries_aap.include_router(sub_category.sub_category_router)
wildberries_aap.include_router(product.product_router)
wildberries_aap.include_router(auth.auth_router)
wildberries_aap.include_router(review.review_router)

setup_admin(wildberries_aap)

if __name__ == '__main__':
    uvicorn.run(wildberries_aap, host='127.0.0.1', port=8001)




