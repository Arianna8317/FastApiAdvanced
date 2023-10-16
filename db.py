from settings import settings
import databases
import sqlalchemy
# from fastapi import FastAPI
# from pydantic import BaseModel
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.types import Boolean, String

DATABASE_URL = settings.DATABASE_URL

database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

products = sqlalchemy.Table(
    "products",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(32)),
    sqlalchemy.Column("description", sqlalchemy.String(128)),
    sqlalchemy.Column("price", sqlalchemy.Integer),
   )
users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(32)),
    sqlalchemy.Column("email", sqlalchemy.String(128)),
    sqlalchemy.Column("password", sqlalchemy.String(128)),
    sqlalchemy.Column("surname", sqlalchemy.String(128)),
)

orders = sqlalchemy.Table(
    "orders",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("user_id", sqlalchemy.Integer, ForeignKey(users.id)),
    sqlalchemy.Column("product_id", sqlalchemy.Integer, ForeignKey(products.id)),
    sqlalchemy.Column("creation_date", sqlalchemy.Date),
    sqlalchemy.Column("description", sqlalchemy.String(128)),
    sqlalchemy.Column("status", sqlalchemy.Boolean),
)


engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
metadata.create_all(engine)