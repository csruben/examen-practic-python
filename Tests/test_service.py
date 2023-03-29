from Domain.nota_validator import NotaValidator
from Domain.sesiune_validator import SesiuneValidator
from Repository.json_repository import JsonRepository
from Service.nota_service import NotaService
from Service.sesiune_service import SesiuneService
from Utils.clear_file import clear_file


def test_service():
    clear_file('test_nota_service.json')
    clear_file('test_sesiune_service.json')

    sesiune_repostiory_test = JsonRepository('test_sesiune_service.json')
    nota_repository_test = JsonRepository('test_nota_service.json')

    nota_validator_test = NotaValidator()
    sesiune_validator_test = SesiuneValidator()

    nota_service = NotaService(nota_repository_test,
                               nota_validator_test)
    sesiune_service = SesiuneService(sesiune_repostiory_test,
                                     sesiune_validator_test,
                                     nota_repository_test)

    nota_service.add('1', 7.0, 'Ruben')
    nota_service.add('2', 5.0, 'Ioan')
    assert len(nota_service.get_all()) == 2

    nota_service.add('3', 9.0, 'Mihai')
    nota_service.add('4', 10.0, 'Cosmin')

    note_service = nota_service.get_all()
    assert len(note_service) == 4

    assert note_service[0].id_entity == '1'
    assert note_service[0].valoare == 7.0
    assert note_service[0].nume_examinator == 'Ruben'

    assert note_service[1].id_entity == '2'
    assert note_service[1].valoare == 5.0
    assert note_service[1].nume_examinator == 'Ioan'

    assert note_service[2].id_entity == '3'
    assert note_service[2].valoare == 9.0
    assert note_service[2].nume_examinator == 'Mihai'

    sesiune_service.add('1', 2, ['1', '2'])
    assert len(sesiune_service.get_all()) == 1

    sesiune_service.add('2', 3, ['1', '2', '3'])
    sesiuni = sesiune_service.get_all()
    assert len(sesiuni) == 2

    assert sesiuni[0].id_entity == '1'
    assert sesiuni[0].numar_studenti == 2
    assert sesiuni[0].lista_id_note == ['1', '2']

    sesiuni_examinare_studenti = sesiune_service.sesiuni_ordonate_dupa_numar_studenti()
    assert len(sesiuni_examinare_studenti) == 2

    sesiune_nume_citit = sesiune_service.sesiune_examinator_citit_tastatura('Ruben')
    assert len(sesiune_nume_citit) == 2

    sesiune_nume_citit = sesiune_service.sesiune_examinator_citit_tastatura('Ioan')
    assert len(sesiune_nume_citit) == 2

    sesiune_nume_citit = sesiune_service.sesiune_examinator_citit_tastatura('Cosmin')
    assert len(sesiune_nume_citit) == 0

    sesiune_service.export_json('test_export.json')

    try:
        with open('test_export.json', 'r'):
            pass
        assert True
    except Exception:
        assert False
