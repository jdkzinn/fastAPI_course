from backend.models import db
from sqlalchemy.orm import sessionmaker # type: ignore

def pegar_sessao():
    Session = sessionmaker(bind=db)
    session = Session()
    Session = sessionmaker(bind=db.engine)
    return Session()