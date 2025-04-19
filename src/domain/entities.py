# domain/entities.py

from dataclasses import dataclass

@dataclass
class Page:
    id: int
    url: str
    level: int
    hash_content: str
    from_id: int
