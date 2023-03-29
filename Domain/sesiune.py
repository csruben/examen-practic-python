from dataclasses import dataclass
from typing import List

from Domain.entity import Entity


@dataclass
class Sesiune(Entity):
    numar_studenti: int
    lista_id_note: List
