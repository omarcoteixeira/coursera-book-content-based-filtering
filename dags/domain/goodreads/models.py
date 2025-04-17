from typing import Union

from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Book(Base):
    __tablename__ = "company"

    iban = Column(String, primary_key=True)
    company_id = Column(Integer)
    name = Column(String)
    address = Column(String)
    country_code = Column(String)


DataTypes = Union[Book]
