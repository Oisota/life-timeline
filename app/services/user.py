from passlib.hash import argon2

from app.exts.sqla import db
from app.models import User


def get_user(user_id):
    """Get a user by email"""
    return db.session.execute(db.select(User).where(User.id == user_id)).scalar()


def add_user(email, password):
    """Add a user to the database"""
    password_hash = argon2.hash(password)
    user = User(email=email, password_hash=password_hash)
    db.session.add(user)
    db.session.commit()


def validate_credentials(email, password):
    """Validate user email and password"""
    stmt = db.select(User).where(User.email == email)
    user = db.session.execute(stmt).scalar()

    if not user:
        return None

    valid = argon2.verify(password, user.password_hash)
    if not valid:
        return None

    return user
