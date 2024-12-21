"""User model definition"""

from sqlalchemy import Column, String
from sqlalchemy.orm import Mapped

from cashcow.models.base import ORMModel

__all__: tuple[str, ...] = ("User",)


class User(ORMModel):
    """User model"""

    __tablename__: str = "users"

    email: Mapped[str] = Column(String, nullable=False)
    """Email of the user"""
    password: Mapped[str] = Column(String, nullable=False)
    """Password of the user"""

    def __repr__(self) -> str:
        return f"<User {self.email!r}>"

    def __str__(self) -> str:
        return self.__repr__()
