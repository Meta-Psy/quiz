import pydantic
from fastapi import FastAPI, Request
from api.users_api.users import user_router
from api.test_api.tests import test_router
from database import Base, engine
app = FastAPI(docs_url='/')
# делаем миграции
Base.metadata.create_all(bind=engine)
# регистрируем компонент (роутер)
app.include_router(user_router)
app.include_router(test_router)
