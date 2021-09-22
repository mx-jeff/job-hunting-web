from factory import init_db, init_app


app = init_app()
db = init_db(app)


class Status(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    status = db.Column(db.String)
