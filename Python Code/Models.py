from peewee import *

mysql_db = MySQLDatabase(
    'pet_project',  # database name
    user='root',  # user name
    password='root',  # password
    host='localhost'  # hostname -> localhost or 127.0.0.1
)


# Define table
class Bank(Model):
    id = PrimaryKeyField(null=False)
    bank_name = CharField(max_length=255)
    bank_address = CharField(max_length=255)
    phone_number = IntegerField()

    class Meta:
        database = mysql_db
        db_table = "Bank"


def insertIntoDb():
    row = Bank(bank_name="LenasBank",bank_address="555 5th Ave, NY NY 10025",phone_number=2125551155)
    row.save()

insertIntoDb()