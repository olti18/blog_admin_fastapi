from sqlalchemy import Boolean, Column, Integer, String, DateTime
from Backend.src.database.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), unique=True, index=True)
    hashed_password = Column(String(255))
    role = Column(String(50), default='user')  

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), index=True)
    content = Column(String(1000))  
    author_id = Column(Integer, index=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True, index=True)
    post_id = Column(Integer, index=True)
    author_id = Column(Integer, index=True)
    content = Column(String(1000))  
    created_at = Column(DateTime)
    updated_at = Column(DateTime)


# class User(Base):
#     __tablename__ = "users"

#     id = Column(Integer, primary_key=True, index=True)
#     username = Column(String, unique=True, index=True)
#     hashed_password = Column(String)



# class Post(Base):
#     __tablename__ = 'posts'
#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String(200), index=True)
#     content = Column(String(1000))  
#     author_id = Column(Integer, index=True)
#     created_at = Column(DateTime)
#     updated_at = Column(DateTime)

# class Comment(Base):
#     __tablename__ = 'comments'
#     id = Column(Integer, primary_key=True, index=True)
#     post_id = Column(Integer, index=True)
#     author_id = Column(Integer, index=True)
#     content = Column(String(1000))  
#     created_at = Column(DateTime)
#     updated_at = Column(DateTime)