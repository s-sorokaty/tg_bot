from db.engine import Base
from sqlalchemy import asc
from sqlalchemy.orm import Session
from sqlalchemy.dialects.sqlite import insert
from sqlalchemy import Table, Column, ForeignKey, Integer, DateTime, VARCHAR, Float

class Result(Base):
    __tablename__ = 'Result'
    message_id = Column(Integer, primary_key=True, nullable=False)
    chat_id = Column(Integer, primary_key=True, nullable=False)
    question_id = Column(Integer, primary_key=True, nullable=False) 
    answer = Column(VARCHAR(255), nullable=True)

    @staticmethod
    def create_db_model(message_id:int, chat_id:int, question_id:int, answer:str):
        return Result(
            message_id=message_id,
            chat_id=chat_id,
            question_id=question_id,
            answer=answer,
        )
    @staticmethod
    def add_result(message_id:int, chat_id:int, question_id:int, answer:str, session:Session):
        statement = insert(Result)\
            .values(message_id=message_id, chat_id=chat_id, question_id=question_id, answer=answer)\
            .on_conflict_do_update(set_=dict(answer=answer))
        
        session.execute(statement)
        session.commit()
    
    @staticmethod
    def get_all(message_id:int, chat_id:int, session:Session):
        res = session.query(Result).filter(Result.message_id==message_id, Result.chat_id==chat_id).order_by(asc(Result.question_id))
        return res.all()
    
    @staticmethod
    def get_result_by_question(message_id:int, chat_id:int, question_id:str, session:Session):
        res = session.query(Result).filter(Result.message_id==message_id, Result.chat_id==chat_id, Result.question_id==question_id)
        return res.all()

class UserInfo(Base):
    __tablename__ = 'UserInfo'
    chat_id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, primary_key=True, nullable=False) 
    username = Column(VARCHAR(255), nullable=False) 
    name = Column(VARCHAR(255), nullable=True)

    @staticmethod
    def add_user(chat_id:int, user_id:int, username:str, name:str, session:Session):
        statement = insert(UserInfo)\
            .values(chat_id=chat_id, user_id=user_id, username=username, name=name)\
            .on_conflict_do_update(set_=dict(username=username, name=name))
        
        session.execute(statement)
        session.commit()

    @staticmethod
    def get_user_by_chat_id(chat_id:int, session:Session):
        res = session.query(UserInfo).filter(UserInfo.chat_id==chat_id)
        return res.first()

#This table have chat to send result of test
class LogChats(Base):
    __tablename__ = 'LogChats'
    chat_id = Column(Integer, primary_key=True, nullable=False)

    @staticmethod
    def add_chat(chat_id:int, session:Session):
        statement = insert(LogChats)\
            .values(chat_id=chat_id)\
            .on_conflict_do_nothing()
        
        session.execute(statement)
        session.commit()

    @staticmethod
    def get_all(session:Session):
        res = session.query(LogChats)
        return res.all()