from peewee import *
from instagrapi.types import User

db = PostgresqlDatabase(user="ilagorbacev",
                        host="localhost",
                        port="5432",
                        database="ploshadka")


# Определяем базовую модель о которой будут наследоваться остальные
class BaseModel(Model):
    class Meta:
        database = db  # соединение с базой, из шаблона выше


class BloggerORM(BaseModel):
    pk = BigIntegerField(primary_key=True)
    username =

db.close()
