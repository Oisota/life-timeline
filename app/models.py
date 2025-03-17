"""SQLAlchemy DB Models"""
from typing import List
from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Table, Column, ForeignKey, event

from app.exts.sqla import db, Base

class Migrations(db.Model):
    """Dbmate migrations"""
    __tablename__ = 'schema_migrations'
    version: Mapped[str] = mapped_column(primary_key=True)

class User(db.Model):
    """User Model"""
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    email: Mapped[str]
    password_hash: Mapped[str]
    events: Mapped[List["Event"]] = relationship(
        back_populates="user", cascade="all, delete-orphan", init=False
    )

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True
    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

class Event(db.Model):
    """Post Model"""
    __tablename__ = 'event'
    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    timestamp: Mapped[int] = mapped_column(nullable=False)
    title: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user: Mapped["User"] = relationship(back_populates="events")