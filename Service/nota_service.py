from Domain.nota import Nota
from Domain.nota_validator import NotaValidator
from Repository.repository import Repository


class NotaService:
    def __init__(self,
                 nota_repository: Repository,
                 nota_validator: NotaValidator):
        self.nota_repository = nota_repository
        self.nota_validator = nota_validator

    def add(self, id_nota: str, valoare: float, nume_examinator: str):
        """
        Adauga o nota
        :param id_nota: id-ul notei
        :param valoare: valoarea notei
        :param nume_examinator: nume examinator
        :return: o nota
        """
        nota = Nota(id_nota, valoare, nume_examinator)

        self.nota_validator.validate(nota)

        self.nota_repository.create(nota)

    def get_all(self):
        """
        :return: o lista cu toate notele
        """
        return self.nota_repository.read()
