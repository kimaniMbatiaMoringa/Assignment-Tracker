#MASTER table creator IF AND ONLY IF  a students.db file does not exist
#Run only once if that is the case
#DO NOT RUN if students.db already exists in your project folder



#I Repeat, DO NOT RUN if students.db already Present

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

#Check

class Assignment(Base):             #Creates an assignment class

    __tablename__='assignments'     #Creates a table (if it doesnt exist) called "assignments"

    __table_args__=(
        PrimaryKeyConstraint(       #Sets the id as the primary key
            'id',
            name='id_pk'
        ),
        UniqueConstraint(           #makes sure that class instances have a unique name
            'name',
            name='unique_name'
        )
    )

    id = Column(Integer(), primary_key=True)    #Creates a column with data containing the id of the Assignment (Autogenerated sequentially)
    name = Column(String())                     #Creates a column 'name' containing the name data of the object created
    category = Column(String())
    grade = Column(Integer())                    #Creates a column 'grade containing the grade data of the object
    #student_id = Column(Integer(),ForeignKey('student.id'))

    def __init__(self,name,category, grade):
        self.name=name
        self.category = category
        self.grade = grade

    #Ensure grade is not above 100:

    """ def get_grade(self):
        return self._grade
    
    def set_grade(self, value):
        if value > 100 or value < 0:
            print("Invalid Grade! Please enter a valid one")
        else:
            self._grade = value """


if __name__ =='__main__':
    engine = create_engine('sqlite:///students.db')
    Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

student_Kimani = Student("Kimani Mbatia")
student_Johan = Student("Johan Blaskowitz")
student_Joe = Student("Joe Obuya")

assignment1 = Assignment("Vector Calculus", "Calc2", 76)    

session.bulk_save_objects([student_Kimani,student_Johan,student_Joe,assignment1])
session.commit()
