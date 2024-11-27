import os
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import uuid

# 環境変数から接続情報を取得
DATABASE_URL = os.environ.get('DATABASE_URL')
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class Cat(Base):
    __tablename__ = "cats"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String(100), nullable=False)
    age = Column(Integer, nullable=False)
    breed = Column(String(100), nullable=False)
    image_url = Column(String(255))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

def init_db():
    Base.metadata.create_all(engine)

def add_cat(name: str, age: int, breed: str, image_url: str = None) -> str:
    db = SessionLocal()
    try:
        cat = Cat(
            name=name,
            age=age,
            breed=breed,
            image_url=image_url
        )
        db.add(cat)
        db.commit()
        return cat.id
    finally:
        db.close()

def get_all_cats():
    db = SessionLocal()
    try:
        return db.query(Cat).order_by(Cat.created_at.desc()).all()
    finally:
        db.close()
