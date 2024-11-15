import hashlib

from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from saleapp import app, db

class User(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100),nullable=False)
    username = Column(String(100),unique=True, nullable=False)
    password = Column(String(100),nullable=False)
    avatar = Column(String(200),default='https://res.cloudinary.com/dy1unykph/image/upload/v1729842193/iPhone_15_Pro_Natural_1_ltf9vr.webp')
    def __str__(self):
        return self.name

class Category(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    products = relationship('Product', backref='Category', lazy=True)

    def __str__(self):
        return self.name


class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    price = Column(Float, default=0)
    image = Column(String(200), default='https://res.cloudinary.com/dy1unykph/image/upload/v1729842193/iPhone_15_Pro_Natural_1_ltf9vr.webp')
    category_id = Column(Integer, ForeignKey('category.id'), nullable=False)
    def __str__(self):
        return self.name


if __name__ == "__main__":
    with app.app_context():
        pass
        # Tạo cơ sở dữ liệu
        # db.create_all()

        # Tạo dữ liệu trong Category
        # c = Category(name="Mobile")
        # c1 = Category(name="Laptop")
        # c2 = Category(name="Tablet")
        # db.session.add_all([c,c1,c2])
        # db.session.commit()

        # Tạo dữ liệu trong Product
        # import json
        # with open('data/products.json', encoding='utf-8') as f:
        #     products = json.load(f)
        #     for p in products:
        #         prod= Product(**p)
        #         db.session.add(prod)
        #     db.session.commit()

#         Tạo user
#         import hashlib
#         u = User(name="Duc", username="admin", password=hashlib.md5("123".encode('utf-8')).hexdigest())
#         db.session.add(u)
#         db.session.commit()

