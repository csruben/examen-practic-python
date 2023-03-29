from typing import List

import jsonpickle

from Domain.sesiune import Sesiune
from Domain.sesiune_validator import SesiuneValidator
from Repository.repository import Repository


class SesiuneService:
    def __init__(self,
                 sesiune_repository: Repository,
                 sesiune_validator: SesiuneValidator,
                 nota_repository: Repository):
        self.sesiune_repository = sesiune_repository
        self.sesiune_validator = sesiune_validator
        self.nota_repository = nota_repository

    def add(self, id_sesiune: str, numar_studenti: int, lista_id_note: List):
        """
        Creeaza o sesiune
        :param id_sesiune: id sesiune
        :param numar_studenti: numar studenti
        :param lista_id_note: id note
        :return: o sesiune
        """
        sesiune = Sesiune(id_sesiune, numar_studenti, lista_id_note)

        for id_note in sesiune.lista_id_note:
            if self.nota_repository.read(id_note) is None:
                raise ValueError('Lista notelor trebuie sa aiba id-uri valide!')

        self.sesiune_validator.validate(sesiune)

        self.sesiune_repository.create(sesiune)

    def get_all(self):
        """
        :return: o lista cu toate sesiunile
        """
        return self.sesiune_repository.read()

    def sesiuni_ordonate_dupa_numar_studenti(self):
        """
        :return: sesiunile ordonate crescator dupa numarul de studenti
        """
        sesiuni = []
        for sesiune in self.sesiune_repository.read():
            sesiuni.append(sesiune)

        return sorted(sesiuni, key=lambda x: x.numar_studenti, reverse=False)

    def sesiune_examinator_citit_tastatura(self, examinator):
        """
        :param examinator: examinator citit de la tastatura
        :return: Returneaza sesiunile de examinare in care exista cel putin o nota
        data de im examinator cu nume citit de la tastatura
        """
        sesiuni = []

        for sesiune in self.sesiune_repository.read():
            lista_id_note = sesiune.lista_id_note
            nr_aparitii = 0
            for id_nota in lista_id_note:
                nume_examinator = self.nota_repository.read(id_nota).nume_examinator

                if nume_examinator == examinator:
                    nr_aparitii += 1
            if nr_aparitii > 0:
                sesiuni.append(sesiune)

        return sesiuni

    def export_json(self, filename):
        """
        Scrierea intr-un fisier Json in care cheile sunt id-urile sesiunilor de examinare si valoarea
        asociata unei chei este media aritmetica a notelor din acea sesiune de examinare
        :param filename: nume fisier Json
        """

        sesiuni_cu_note = {}

        for sesiune in self.sesiune_repository.read():
            sesiuni_cu_note[sesiune.id_entity] = 0

        for sesiune in self.sesiune_repository.read():
            lista_note = sesiune.lista_id_note

            for id_nota in lista_note:
                sesiuni_cu_note[sesiune.id_entity] += self.nota_repository.read(id_nota).valoare

            sesiuni_cu_note[sesiune.id_entity] = sesiuni_cu_note[sesiune.id_entity] / sesiune.numar_studenti

        with open(filename, 'w') as f:
            f.write(jsonpickle.dumps(sesiuni_cu_note, indent=2))
