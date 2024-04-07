from peewee import *


db = SqliteDatabase('./app/database/data.db')

class BaseModel(Model):
    id = AutoField()
    class Meta:
        database = db

class User(BaseModel):
    user_id = BigIntegerField(primary_key=True)
    username = CharField(null = True)
    class Meta:
        db_table = 'Users'
