# File chứa các models (tạo models cho database bằng cơ chế orm)
from sqlalchemy import Column, Integer, String
from init import db, app

class BaseModel(db.Model):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)

class User(BaseModel):
    name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    avatar = Column(String(50), nullable=True)

    def __str__(self):
        return self.name

if __name__ == '__main__':
    with app.app_context():
        # Tạo tất cả bảng cho tất cả models vào database
        #db.create_all()

        # Khởi tạo các obj
        # u1 = User(name="Truong", email="truong@gmail.com", avatar=None)
        # u2 = User(name="Truongne", email="truongne@gmail.com", avatar=None)
        # u3 = User(name="Truong123", email="truong123@gmail.com", avatar=None)

        # Add các obj vào session
        # db.session.add_all([u1, u2, u3])

        # Commit session vào database
        # db.session.commit()
        pass



