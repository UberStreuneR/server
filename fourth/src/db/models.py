from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship
import sqlalchemy as sa

Base = declarative_base()

class Client(Base):
    __tablename__ = "clients"
    client_id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)

class Account(Base):
    __tablename__ = "accounts"
    account_id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    client_id = sa.Column(ForeignKey("clients.client_id"), nullable=False)
    client = relationship("Client", backref="accounts")

class LineOfCredit(Base):
    __tablename__ = "lines"
    line_id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)