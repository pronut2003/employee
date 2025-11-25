from mongoengine import (Document, StringField, IntField, DateField, EmailField, LongField)

class Employee(Document):
    ID = IntField(primary_key=True)

    NAME = StringField(required=True, max_length=100)
    GENDER = StringField(required=True, choices=["MALE", "FEMALE", "OTHER"])

    DOB = DateField(required=True)
    DOJ = DateField(required=True)

    DEPARTMENT = StringField(required=True, max_length=50)
    DESIGNATION = StringField(required=True, max_length=50)

    SALARY = LongField(required=True, min_value=0)

    PHONE = StringField(required=True, max_length=15)
    EMAIL = EmailField(required=True, unique=True)

    def __str__(self):
        return f"{self.ID} - {self.NAME} - {self.GENDER} - {self.DOB} - {self.DOJ} - {self.DEPARTMENT} - {self.DESIGNATION} - {self.SALARY} - {self.PHONE} - {self.EMAIL}"