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
    teach_name = CharField()
    teach_email = CharField()
    teach_password = CharField()

    class Meta:
        database = db

Teacher.create_table(fail_silently=True)

class Product(Model):
    prod_price = CharField()
    prod_quantity = CharField()
    prod_description = CharField()
    prod_color = CharField()

    class Meta:
        database = db

Product.create_table(fail_silently=True)

class User(Model):
    user_name = CharField()
    user_phone = CharField()
    user_email = CharField()
    user_password = CharField()


    class Meta:
        database = db

User.create_table(fail_silently=True)
