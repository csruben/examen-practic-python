from Domain.sesiune import Sesiune


class SesiuneValidator:
    def validate(self, sesiune: Sesiune):
        errors = []
        if sesiune.numar_studenti < 1:
            errors.append('Numarul studentilor trebuie sa fie mai mare ca 0 !')
        if len(sesiune.lista_id_note) != sesiune.numar_studenti:
            errors.append('Numarul notelor trebuie sa fie egal cu numarul studentilor!')
        if errors:
            raise ValueError(errors)
