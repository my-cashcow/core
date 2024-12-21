"""Bank model definition"""

from datetime import datetime, timedelta
from decimal import Decimal

from sqlalchemy import Column, DateTime, ForeignKey, Integer, Interval, Numeric, String
from sqlalchemy.orm import Mapped

from cashcow.constants import AccountType, Currency
from cashcow.models.base import MetadataMixin, PipelineORMModel, TimestampMixin

__all__: tuple[str, ...] = (
    "Account",
    "Transaction",
)


class Account(PipelineORMModel, MetadataMixin):
    """Account model"""

    __tablename__: str = "accounts"

    connection_id: Mapped[int] = Column(Integer, ForeignKey("connections.id"), nullable=False)
    """ID of the connection"""

    identifier: Mapped[str] = Column(String, nullable=False)
    """Identifier of the account"""
    name: Mapped[str] = Column(String, nullable=False)
    """Name of the account"""
    type: Mapped[AccountType] = Column(String, nullable=False)
    """Type of the account"""
    currency: Mapped[Currency] = Column(String, nullable=False)
    """Currency of the account"""

    product_name: Mapped[str] = Column(String, nullable=False)
    """Name of the product"""
    product_description: Mapped[str] = Column(String)
    """Description of the product"""

    period: Mapped[timedelta] = Column(Interval)
    """Period of the product"""
    start_date: Mapped[datetime] = Column(DateTime)
    """Start date of the product"""
    end_date: Mapped[datetime] = Column(DateTime)
    """End date of the product"""

    def __repr__(self) -> str:
        return f"<Account {self.name} ({self.identifier})>"

    def __str__(self) -> str:
        return self.__repr__()


class Transaction(PipelineORMModel, TimestampMixin, MetadataMixin):
    """Transaction model"""

    __tablename__: str = "transactions"

    account_id: Mapped[int] = Column(Integer, ForeignKey("accounts.id"), nullable=False)
    """ID of the account"""

    branch: Mapped[str] = Column(String)
    """Branch of the transaction"""
    category: Mapped[str] = Column(String, nullable=False)
    """Category of the transaction"""
    amount: Mapped[Decimal] = Column(Numeric(12, 4), nullable=False)
    """Amount of the transaction"""
    destination: Mapped[str] = Column(String)
    """Identifier of the destination"""
    currency: Mapped[Currency] = Column(String, nullable=False)
    """Currency of the transaction"""

    balance_amount: Mapped[Decimal] = Column(Numeric(12, 4), nullable=False)
    """Balance amount of the account after the transaction (follows the currency of account)"""

    transaction_time: Mapped[datetime] = Column(DateTime, nullable=False)
    """Transaction time"""
