from peewee import *


db = SqliteDatabase('./app/database/data.db')

class BaseModel(Model):
    id = AutoField()
    class Meta:
        database = db

class User(BaseModel):
    user_id = BigIntegerField()
    username = CharField(null = True)
    balance = BigIntegerField(default=10000)
    class Meta:
        db_table = 'Users'
#