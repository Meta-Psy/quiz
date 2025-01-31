from fastapi import APIRouter
from database.testservice import *

test_router = APIRouter(prefix='/test',
                        tags=['Создание тестов'])


@test_router.post('/add_q')
async def add_q(main_q: str, v1: int, v2: int, correct_answer: int, level: str, v3: int, v4: int):
    all_question = add_question_db(main_question=main_q, v1=v1, v2=v2,
                                   correct_answer=correct_answer, v3=v3, v4=v4, level=level)
    if all_question:
        return {"status": 1, "message": all_question}
    return {"status": 0, "message": "Ошибка"}


@test_router.post('/top_5')
async def top_5(level: str):
    u_top_5 = get_top5_db(level=level)
    if u_top_5:
        return {"status": 1, "message": u_top_5}
    return {"status": 0, "message": "Ошибка"}


@test_router.post('/q_20')
async def q_20(level: str):
    u_q_20 = get_20_questions_db(level=level)
    if u_q_20:
        return {"status": 1, "message": u_q_20}
    return {"status": 0, "message": "Ошибка"}
