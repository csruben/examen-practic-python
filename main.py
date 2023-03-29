from Domain.nota_validator import NotaValidator
from Domain.sesiune_validator import SesiuneValidator
from Repository.json_repository import JsonRepository
from Service.nota_service import NotaService
from Service.sesiune_service import SesiuneService
from Tests.test_all import test_all
from UserInterface.Console import Console


def main():
    nota_repository = JsonRepository('nota.json')
    sesiune_repository = JsonRepository('sesiune.json')

    nota_validator = NotaValidator()
    sesiune_validator = SesiuneValidator()

    nota_service = NotaService(nota_repository,
                               nota_validator)
    sesiune_service = SesiuneService(sesiune_repository,
                                     sesiune_validator,
                                     nota_repository)

    console = Console(nota_service, sesiune_service)
    console.run_console()


if __name__ == '__main__':
    test_all()
    main()
