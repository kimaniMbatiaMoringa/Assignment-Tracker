import functools

from sqlalchemy import (create_engine, desc, func,
    CheckConstraint, PrimaryKeyConstraint, UniqueConstraint,
    Index, Column, DateTime, Integer, String)
from sqlalchemy.orm import sessionmaker, relationship

from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Student(Base):
    __tablename__='students'

    __table_args__=(
        PrimaryKeyConstraint(
            'id',
            name='id_pk'
        ),
        UniqueConstraint(
            'name',
            name='unique_name'
        )
    ) 

    id = Column(Integer(),primary_key=True)
    name = Column(String())
    average_grade = Column(Integer())

    def __init__(self, name):
        self.name = name
        self.average_grade = 0
        self.scores = []

    def set_average_grade(self):
        avg = functools.reduce(sum, self.scores)    