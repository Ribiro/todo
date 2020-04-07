from app import db


class DotoModel(db.Model):
    __tablename__ = 'doto'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    email = db.Column(db.String(50), unique=True)
    activity = db.Column(db.String(50))

    # insert into database
    def add_records(self):
        db.session.add(self)
        db.session.commit()
        return self

    # fetch from database
    @classmethod
    def fetch_records(cls):
        return cls.query.all()

    # update by id
    @classmethod
    def update_by_id(cls, id, name=None, email=None, activity=None):
        record = cls.query.filter_by(id=id).first()
        if name:
            record.name = name
        if email:
            record.email = email
        if activity:
            record.activity = activity

        db.session.commit()
        return True
