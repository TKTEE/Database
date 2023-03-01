from peewee import *
from os import path

connection = path.dirname(path.realpath(__file__))
db = SqliteDatabase(path.join(connection, "Tony.db"))

#creating our first table

class Student(Model):
    stud_name = CharField()
    stud_email = CharField()
    stud_password = CharField()
    class Meta:
        database = db

Student.create_table(fail_silently=True)

class Teacher(Model):
    Teach_name = CharField()
    Teach_email = CharField()
    Teach_password = CharField()

    class Meta:
        database = db

Teacher.create_table(fail_silently=True)

class Product(Model):
    Prod_price = CharField()
    Prod_quantity = CharField()
    Prod_description = CharField()
    Prod_color = CharField()

    class Meta:
        database = db

Product.create_table(fail_silently=True)

class User(Model):
    User_name = CharField()
    User_phone = CharField()
    User_email = CharField()
    User_password = CharField()


    class Meta:
        database = db

User.create_table(fail_silently=True)
