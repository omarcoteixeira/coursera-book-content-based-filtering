from typing import Union

from sqlalchemy import Column, String, Integer, BigInteger, Table, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


book_authors = Table(
    'book_authors', Base.metadata,
    Column('book_id', String, ForeignKey('book.isbn'), primary_key=True),
    Column('author_id', Integer, ForeignKey('author.id'), primary_key=True)
)

class Book(Base):
    __tablename__ = "book"

    isbn = Column(String, primary_key=True)
    isbn13 = Column(BigInteger, nullable=False)
    title = Column(String, nullable=False)
    average_rating = Column(Integer, nullable=False, default=0)
    language_code = Column(String)
    num_pages = Column(Integer, default=0)
    ratings_count = Column(Integer)
    text_reviews_count = Column(Integer)
    publication_date = Column(String)
    publisher = Column(String)
    
    authors = relationship("Author", secondary=book_authors, back_populates="books")


class Author(Base):
    __tablename__ = 'author'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    books = relationship("Book", secondary=book_authors, back_populates="authors")


DataTypes = Union[Book, Author]
