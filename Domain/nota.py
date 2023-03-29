from dataclasses import dataclass

from Domain.entity import Entity


@dataclass
class Nota(Entity):
    valoare: float
    nume_examinator: str
