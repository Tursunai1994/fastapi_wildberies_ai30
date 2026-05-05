
from fastapi import FastAPI
from api import user,category,sub_category,product,auth,review
import uvicorn
from admin.setup import setup_admin



wildberies_aap = FastAPI(title= 'FastAPI Wildberies ai30')
wildberies_aap.include_router(user.user_router)
wildberies_aap.include_router(category.category_router)
wildberies_aap.include_router(sub_category.sub_category_router)
wildberies_aap.include_router(product.product_router)
wildberies_aap.include_router(auth.auth_router)
wildberies_aap.include_router(review.review_router)

setup_admin(wildberies_aap)

if __name__ == '__main__':
    uvicorn.run(wildberies_aap, host='127.0.0.1', port=8001)




