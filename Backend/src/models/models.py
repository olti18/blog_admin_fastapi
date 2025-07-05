from sqlalchemy import Boolean, Column, Integer, String, DateTime
from Backend.src.database.database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    email = Column(String(100), unique=True, index=True)
    password = Column(String(100))
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), index=True)
    content = Column(String(1000))  # <-- removed index=True
    author_id = Column(Integer, index=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True, index=True)
    post_id = Column(Integer, index=True)
    author_id = Column(Integer, index=True)
    content = Column(String(1000))  # <-- removed index=True
    created_at = Column(DateTime)
    updated_at = Column(DateTime)