from database import Base
from sqlalchemy import (Column, Integer, String, BigInteger,
                        DateTime, Boolean, ForeignKey)
from sqlalchemy.orm import relationship
from datetime import datetime


# создаём модель юзеров
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, nullable=False)
    phone_number = Column(String, unique=True)
    reg_date = Column(DateTime, default=datetime.now())

class Question():
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True, autoincrement=True)
    main_question = Column(String, nullable=False)
    v1 = Column(String, nullable=False)
    v2 = Column(String, nullable=False)
    v3 = Column(String, nullable=True)
    v4 = Column(String, nullable=True)
    correct_answer = Column(Integer)
    level = Column(String, default='Beginner')
    # timer = Column(Integer, default=45)


class UserAnswer(Base):
    __tablename__ = 'user_answers'
    id = Column(Integer, autoincrement=True, primary_key=True)
    level = Column(Integer, ForeignKey('users.id'))
    question_id = Column(Integer, ForeignKey('questions.id'))
    user_answer = Column(Integer, nullable=True)
    correctness = Column(Boolean, default=False)
    level = Column(String)
    # создание связей
    user_fk = relationship(User, lazy='subquery')
    question_fk = relationship(Question, lazy='subquery')

class Rating(Base):
    id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(Integer, autoincrement=True)
    correct_answers = Column(Integer)
    level = Column(Integer)




