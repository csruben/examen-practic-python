from Domain.nota import Nota


class NotaValidator:
    def validate(self, nota: Nota):
        errors = []
        if nota.valoare < 1 or nota.valoare > 10:
            errors.append('Nota trebuie sa fie intre 1 si 10!')
        if errors:
            raise ValueError(errors)
