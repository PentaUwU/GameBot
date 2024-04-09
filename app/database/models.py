from peewee import *
from datetime import datetime

db = SqliteDatabase('./app/database/data.db')

class BaseModel(Model):
    id = AutoField()
    class Meta:
        database = db

class Group(BaseModel):
    group_name = CharField(primary_key=True)
    group_balance =BigIntegerField(default=0)
    group_lvl = IntegerField(default=0)
    group_xp = IntegerField(default=0)
    group_users_count = IntegerField(default=1)

class User(BaseModel):
    user_id = BigIntegerField(primary_key=True)
    username = CharField(null=True)
    balance = BigIntegerField(default=10000)
    last_bonus_claim = DateTimeField(default=datetime.min)
    user_lvl = IntegerField(default=1)
    user_xp = IntegerField(default=0)
    group_name = ForeignKeyField(Group, null=True)

# class Work(BaseModel):
#     work_name = CharField(primary_key=True)
#     reward = IntegerField(default=10)
#     time = TimeField()

    
