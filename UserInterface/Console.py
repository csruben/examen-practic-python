from Service.nota_service import NotaService
from Service.sesiune_service import SesiuneService


class Console:
    def __init__(self,
                 nota_service: NotaService,
                 sesiune_service: SesiuneService):
        self.nota_service = nota_service
        self.sesiune_service = sesiune_service

    def print_menu(self):
        print('1. Adaugare nota')
        print('2. Adaugare sesiune')
        print('a1. Afisare note')
        print('a2. Afisare sesiuni')
        print('3. Afisare sesiuni ordonate crescator dupa nr de studenti')
        print('4. Afisare sesiuni in care exista cel putin o nota data '
              'de un examinator cu nume citit de la tastatura')
        print('5. Export Json in care cheile sunt id-urile sesiunilor de examinare si valoarea asociata unei chei'
              'este media aritmetica a notelor din acea sesiune de examinare')
        print('x. Iesire')

    def run_console(self):
        while True:
            self.print_menu()
            opt = input('Introducere optiune: ')
            if opt == 'x':
                break
            elif opt == '1':
                self.handle_add_nota()
            elif opt == '2':
                self.handle_add_sesiune()
            elif opt == 'a1':
                self.show_all(self.nota_service.get_all())
            elif opt == 'a2':
                self.show_all(self.sesiune_service.get_all())
            elif opt == '3':
                self.afisare_sesiuni_ordonate()
            elif opt == '4':
                self.afisare_sesiune_examinator_citit_tastatura()
            elif opt == '5':
                self.export_json_medie_aritmetica()
            else:
                print('Reincercati! Necunoscut!')

    def show_all(self, entities):
        for entity in entities:
            print(entity)

    def handle_add_nota(self):
        try:
            id_nota = input('Id nota: ')
            valoare = float(input('Valoare: '))
            nume_examinator = input('Nume examinator: ')

            self.nota_service.add(id_nota, valoare, nume_examinator)
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def handle_add_sesiune(self):
        try:
            id_sesiune = input('Id sesiune: ')
            numar_studenti = int(input('Numar studenti: '))
            lista_id_note_str = input('Introduceti id note despartite prin ,')
            lista_id_note = list(lista_id_note_str.split(','))

            self.sesiune_service.add(id_sesiune, numar_studenti, lista_id_note)
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def afisare_sesiuni_ordonate(self):
        try:
            print(self.sesiune_service.sesiuni_ordonate_dupa_numar_studenti())
        except Exception as e:
            print(e)

    def afisare_sesiune_examinator_citit_tastatura(self):
        try:
            examinator = input('Nume examinator: ')
            print(self.sesiune_service.sesiune_examinator_citit_tastatura(examinator))
        except Exception as e:
            print(e)

    def export_json_medie_aritmetica(self):
        try:
            filename = input('filename: ')

            self.sesiune_service.export_json(filename)
        except Exception as e:
            print(e)
