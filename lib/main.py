import ipdb

from sqlalchemy import (create_engine, desc, func,
    CheckConstraint, PrimaryKeyConstraint, UniqueConstraint,ForeignKey,
    Index, Column, DateTime, Integer, String)
from sqlalchemy.orm import sessionmaker

from sqlalchemy.orm import declarative_base,relationship

from classes.Student import Student
from classes.Assignment import Assignment

import functools

Base = declarative_base()           #Allows classes to be mapped to tables when they are created

#note you cannot create a db from an external class import since the Base schema is external
  

""" def check_input(task):
    if task == 1:
        print("Create A student")
        student_input = input("Enter Student Name")
        student_input = Student(student_input)
    elif task == 3:
        print("Create Assignment)

    else:
        print("Others pending")
 """

student_Kimani = Student("Kimani Mbatia")

#assignment1 = Assignment("Vector Calculus", "Calc2", 76)

#Should this method be used????:

if __name__ =='__main__':
    engine = create_engine('sqlite:///students.db', echo=True)
    Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def createStudent():
    print("Welcome to the student creation page")
    name_input = input("Please type in the students name:")
    new_student_obj =Student(name_input)
    session.add(new_student_obj)
    session.commit()

def searchStudents():
    print("put in the name of the student you wish to search for")
    term = input()
    searchresp = session.query(Student).filter(Student.name == term).first()
    #searchresp = session.query(Student).filter(Student.name.like('%term%'))    #returns names in the table that are similar to the search term
    #print([searchresp for searchresp in searchresp])
    print("We Found:","\n","ID: ", searchresp.id , "Name: ", searchresp.name,)
    #for i in searchresp:
    #    print("We Found:","\n","ID: ", i.id , "Name: ", i.name,)
    #return searchresp

def all_students():
    print("Here is a list of all the students:")
    for student in session.query(Student):
        print(student.name)
    #student_data = session.query(Student).all()
    #print(student_data)


def all_assignments():
    print("Here are all the assignments: ")
    for assignment in session.query(Assignment):
        print(assignment.name)


print("Welcome to the Student tracker application")
print("\n Select what you want to do")

print("\n 1. Create Student Profile")
print("\n 2. Search Students")
print("\n 3. Show All Students")
print("\n 2. Create Assignment")
print("\n 3. View Assignments")
print("\n 4. Search Students")

task = input("Enter what you want to do: ")
print(task)
if task == 1:
    createStudent()

ipdb.set_trace()