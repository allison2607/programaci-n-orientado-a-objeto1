from decouple import config
from peewee import MySQLDatabase


def conectar():
    database = MySQLDatabase(config('DB_NAME'), **{
        'charset': 'utf8mb4',
        'host': config('DB_HOST'),
        'port': config('DB_PORT', cast=int),
        'user': config('DB_USER'),
        'password': config('DB_PASSWORD')})
    return database