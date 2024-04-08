from peewee import *
from datetime import datetime

db = SqliteDatabase('./app/database/data.db')

class BaseModel(Model):
    id = AutoField()
    class Meta:
        database = db

class User(BaseModel):
    user_id = BigIntegerField()
    username = CharField(null=True)
    balance = BigIntegerField(default=10000)
    last_bonus_claim = DateTimeField(default=datetime.min)
    user_lvl = IntegerField(default=1)
    user_xp = IntegerField(default=560)
    class Meta:
        db_table = 'Users'

class TopPlayer(BaseModel):
    user = ForeignKeyField(User, backref='top_player')
    money_rank = IntegerField(default=0)
    xp_rank = IntegerField(default=0)
    class meta:
        db_table = 'TopPlayers'