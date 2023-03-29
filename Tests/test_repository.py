from dataclasses import dataclass

from Domain.entity import Entity
from Repository.json_repository import JsonRepository
from Utils.clear_file import clear_file


@dataclass
class ClasaTest(Entity):
    pb1: str
    pb2: str


def test_repo():
    clear_file("test_repository.json")
    repo = JsonRepository("test_repository.json")

    clasa_1 = ClasaTest('1', '1', '1')
    clasa_2 = ClasaTest('2', '2', '2')
    clasa_3 = ClasaTest('3', '3', '3')
    clasa_4 = ClasaTest('4', '4', '4')

    repo.create(clasa_1)
    assert len(repo.read()) == 1
    try:
        repo.create(clasa_1)
        assert False
    except KeyError:
        assert True

    repo.create(clasa_2)
    repo.create(clasa_3)
    assert len(repo.read()) == 3

    repo.create(clasa_4)
    assert len(repo.read()) == 4

    repos = repo.read()
    assert len(repos) == 4

    assert repos[0].id_entity == "1"
    assert repos[0].pb1 == "1"
    assert repos[0].pb2 == "1"

    assert repos[1].id_entity == "2"
    assert repos[1].pb1 == "2"
    assert repos[1].pb2 == "2"

    assert repos[2].id_entity == "3"
    assert repos[2].pb1 == "3"
    assert repos[2].pb2 == "3"

    assert repos[3].id_entity == "4"
    assert repos[3].pb1 == "4"
    assert repos[3].pb2 == "4"

    repo.delete('4')
    assert len(repo.read()) == 3

    repo.update(ClasaTest('1', '5', '5'))
    repo.update(ClasaTest('2', '5', '5'))
    repos = repo.read()
    assert len(repos) == 3

    assert repos[0].id_entity == "1"
    assert repos[0].pb1 == "5"
    assert repos[0].pb2 == "5"

    assert repos[1].id_entity == "2"
    assert repos[1].pb1 == "5"
    assert repos[1].pb2 == "5"

    assert repos[2].id_entity == "3"
    assert repos[2].pb1 == "3"
    assert repos[2].pb2 == "3"

    repo.delete('1')
    assert len(repo.read()) == 2
    repo.delete('2')
    assert len(repo.read()) == 1
    repo.delete('3')
    assert len(repo.read()) == 0
    try:
        repo.delete('23')
        assert False
    except Exception:
        assert True
