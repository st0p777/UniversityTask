from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy_imageattach.entity import Image, image_attachment


Base = declarative_base()


class User(Base):
    __tablename__ = "User"
    id = Column(Integer, primary_key=True)
    username = Column(String(60))
    first_name = Column(String(60), nullable=True)
    last_name = Column(String(60), nullable=True)
    email = Column(String(30))
    picture = image_attachment('UserPicture')


class UserPicture(Base, Image):
    __tablename__ = 'User_image'
    user_id = Column(Integer, ForeignKey('User.id'), primary_key=True)
    user = relationship('User')
