from typing import Union

from sqlalchemy import Column, String, Integer, ForeignKey, Identity, Table
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Book(Base):
    __tablename__ = "book"

    isbn = Column(String, primary_key=True)
    isbn13 = Column(String, nullable=False)
    title = Column(String, nullable=False)
    average_rating = Column(Integer, nullable=False, default=0)
    language_code = Column(String)
    num_pages = Column(Integer)
    ratings_count = Column(Integer)
    text_reviews_count = Column(Integer)
    publication_date = Column(String)
    publisher = Column(String)
    authors = Column(String)


DataTypes = Union[Book]
