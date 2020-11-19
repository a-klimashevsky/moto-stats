from dataclasses import dataclass


@dataclass
class Offer:
    id: str
    mark: str
    model: str
    price: float
    year: int
