from db.engine import Base
from sqlalchemy.orm import Session
from sqlalchemy import Table, Column, ForeignKey, Integer, DateTime, VARCHAR, Float
from sqlalchemy.dialects.sqlite import insert

class Result(Base):
    __tablename__ = 'Result'
    message_id = Column(Integer, primary_key=True, nullable=False)
    chat_id = Column(Integer, primary_key=True, nullable=False)
    question_id = Column(Integer, primary_key=True, nullable=False) 
    answer = Column(VARCHAR(255), nullable=True)

    def create_db_model(self, message_id:int, chat_id:int, question_id:int, answer:str):
        return Result(
            message_id=message_id,
            chat_id=chat_id,
            question_id=question_id,
            answer=answer,
        )
    
    def add_result(self, message_id:int, chat_id:int, question_id:int, answer:str, session:Session):
        statement = insert(Result)\
            .values(message_id=message_id, chat_id=chat_id, question_id=question_id, answer=answer)\
            .on_conflict_do_update(set_=dict(answer=answer))
        
        session.execute(statement)
        session.commit()