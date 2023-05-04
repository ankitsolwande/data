from mypro import db
class Users(db.Model):
    __tablename__='users'
    id=db.Column("id",db.Integer,primary_key=True)
    name=db.Column("name",db.String(100),nullable=False)
    password=db.Column("password",db.String(100))

    def __repr__(self):
        return {
            'name':self.name,
            'password':self.password
        }

        