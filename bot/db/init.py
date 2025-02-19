from db.engine import engine
from db.db_model import Base


def init():
    Base.metadata.create_all(bind=engine)