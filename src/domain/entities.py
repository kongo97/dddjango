# domain/entities.py

from dataclasses import dataclass
from datetime import date
from decimal import Decimal

@dataclass
class Invoice:
    id: int
    customer_name: str
    amount: Decimal
    issued_date: date
