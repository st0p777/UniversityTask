from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy_imageattach.entity import Image, image_attachment


Base = declarative_base()


class ProductCategory(Base):
    __tablename__ = "ProductCategory"
    id = Column(Integer, primary_key=True)
    name = Column(String(60))
    description = Column(String(200), nullable=True)


class Product(Base):
    __tablename__ = "Product"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    image = image_attachment('ProductPicture')
    description = Column(String(400))
    s_description = Column(String(80), nullable=False)
    price = Column(Integer, nullable=False)
    quantity = Column(Integer)
    category = relationship("ProductCategory")


class ProductPicture(Base, Image):
    __tablename__ = 'Product_image'
    user_id = Column(Integer, ForeignKey('Product.id'), primary_key=True)
    product = relationship('Product')


class Basket(Base):
    __tablemane__ = "Basket"
    id = Column(Integer, primary_key=True)
    user = Column(Integer, ForeignKey("User.id"), nullable=False)
    product = Column(Integer, ForeignKey("Product.id"), nullable=False)
    count = Column(Integer)

