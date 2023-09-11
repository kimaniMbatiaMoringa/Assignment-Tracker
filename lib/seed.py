import ipdb

from sqlalchemy import (create_engine, desc, func,
    CheckConstraint, PrimaryKeyConstraint, UniqueConstraint,ForeignKey,
    Index, Column, DateTime, Integer, String)
from sqlalchemy.orm import sessionmaker

from sqlalchemy.orm import declarative_base,relationship

from classes.Student import Student
from classes.Assignment import Assignment


Base = declarative_base() 

if __name__ =='__main__':
    engine = create_engine('sqlite:///students.db')
    Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

#student_Kimani = Student("Kimani Mbatia")
student_Johan = Student("Johan Blaskowitz")
student_Joe = Student("Joe Obuya")

#session.add(student_Kimani)
session.add(student_Johan)
session.add(student_Joe)
session.commit()
#assignment1 = Assignment("Vector Calculus", "Calc2", 76)