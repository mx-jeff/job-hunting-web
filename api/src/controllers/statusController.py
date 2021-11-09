from factory import db
from src.Models.database import Status


def create_db():
    db.create_all()


def insert(target):
    create_db()
    data = Status(status=target)
    db.session.add(data)
    db.session.commit()


def remove_db():
    try:
        db.session.query(Status).delete()
        db.session.commit()
        print('Deletado com sucesso!')
    except Exception:
        db.session.rollback()


def selectAll():
    data = db.session.query(Status.status).all()
    # print(str(data))
    return data