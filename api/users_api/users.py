from fastapi import APIRouter
from database.userservice import *


user_router = APIRouter(prefix='/user',
                        tags=['Пользовательская часть'])


@user_router.post('/register')
async def add_user(username: str, phone_number: str):
    u_result = add_user_db(name=username, phone_number=phone_number)
    if u_result:
        return {"status": 1, "message": u_result}
    return {"status": 0, "message": "Ошибка"}


@user_router.post('/answer')
async def answer(user_id: int, q_id: int, level: str, user_answer: int):
    u_answer = user_answer_db(user_id=user_id, q_id=q_id, level=level, user_answer=user_answer)
    if u_answer:
        return {'status': 1, 'message': u_answer}
    return {'status': 0, 'message': 'Ошибка'}


@user_router.post('/result')
async def result(user_id: int):
    u_result = result_db(user_id=user_id)
    if u_result:
        return {'status': 1, 'message': u_result}
    return {'status': 0, 'message': 'Ошибка'}


@user_router.post('/rating')
async def rating(user_id: int, level: str):
    u_rating = rating_db(user_id=user_id, level=level)
    if u_rating:
        return {'status': 1, 'message': u_rating}
    return {'status': 0, 'message': 'Ошибка'}
