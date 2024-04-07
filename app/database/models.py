from peewee import *
from datetime import datetime

db = SqliteDatabase('./app/database/data.db')

class BaseModel(Model):
    id = AutoField()
    class Meta:
        database = db

class User(BaseModel):
    user_id = BigIntegerField()
    username = CharField(null = True)
    balance = BigIntegerField(default=10000)
    last_bonus_claim = DateTimeField(default=datetime.now)
    class Meta:
        db_table = 'Users'
#