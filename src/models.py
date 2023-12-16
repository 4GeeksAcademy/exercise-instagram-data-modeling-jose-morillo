import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(250), unique=True, nullable=False)
    email = Column(String(250), unique=True, nullable=False)
    first_name = Column(String(250), nullable=True)
    last_name = Column(String(250), nullable=True)
    posts = relationship("posts", back_populates="users") 
    Likes = relationship("likes", back_populates="users")
    comments = relationship("comments", back_populates="users")
 
class Posts(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True)
    caption = Column(String(250), nullable=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    users = relationship("users", back_populates="posts")
    media = relationship("media", back_populates="posts")

class Comments(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True)
    body = Column(String(250), nullable=False)
    author_id = Column(Integer, ForeignKey("users.id"))
    post_id = Column(Integer, ForeignKey("posts.id"))
    users = relationship("users", back_populates="comments")


class Likes(Base):
    __tablename__ = "likes"
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey("posts.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    users = relationship("users", back_populates="likes")


class Media(Base):
    __tablename__ = "media"
    id = Column(Integer, primary_key=True)
    url = Column(String(250), nullable=False)
    post_id = Column(Integer, ForeignKey("posts.id"))
    posts = relationship("posts", back_populates="media")

    


## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
