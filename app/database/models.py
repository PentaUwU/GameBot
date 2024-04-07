from peewee import *


db = SqliteDatabase('./app/database/data.db')

class BaseModel(Model):
    id = AutoField()
    class Meta:
        database = db

class User(BaseModel):
    user_id = BigIntegerField()
    username = CharField(null = True)
    class Meta:
        db_table = 'Users'
#