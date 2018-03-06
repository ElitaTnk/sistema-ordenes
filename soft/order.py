#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Author: ElitaTnk
Github: https://github.com/ElitaTnk

Orders
Orders are enumerated objects, with a date of creation, date of payment, user
who created it. Orders can be listed and filtered by date, number, creator.

"""

from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.sql import func

Base = declarative_base()


class Order(Base):
    __tablename__ = 'order'
    id = Column(Integer, primary_key=True)
    creation_date = Column(DateTime(timezone=True), server_default=func.now())
#    _close_order = Column()

#    def closeOrder(self):
#        return datetime.now().strftime('%Y-%m-%d %H:%M:%S')


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    order_id = Column(Integer, ForeignKey('order.id'))
    order = relationship(Order)


# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
engine = create_engine('sqlite:///sqlalchemy_example.db')

# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)
