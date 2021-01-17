from schedule import Schedule
from module import Module
from task import Task
from utils import input_number
import datetime
import os

# TODO secure inputs from warnings
class ParentInterface:
    def __init__(self, available_modules: list):
        self.schedule = Schedule()
        self.available_modules = available_modules

    def edit_module(self):
        print("Jakie zadanie chcesz edytować? (podaj numer od 1 do " + str(len(self.available_modules)) + ")")
        chosen_module = -1
        while chosen_module not in range(1, len(self.available_modules) + 1):
            chosen_module = input_number(">> ")
        chosen_module -= 1
        self.available_modules[chosen_module].print_module()
        print("Chcesz dodać nową nazwę? (t, n)")
        edit = 'z'
        while edit not in ['t', 'n']:
            edit = input(">> ")
        if edit == 't':
            self.available_modules[chosen_module].name = input("Wprowadź nazwę\n>> ")
        print("Chcesz dodać nowy obraz? (t, n)")
        edit = 'z'
        while edit not in ['t', 'n']:
            edit = input(">> ")
        if edit == 't':
            self.available_modules[chosen_module].image = input("Wprowadź link do obrazu\n>> ")
        print("Chcesz dodać nowy opis? (t, n)")
        edit = 'z'
        while edit not in ['t', 'n']:
            edit = input(">> ")
        if edit == 't':
            self.available_modules[chosen_module].description = input("Wprowadź opis\n>> ")

    def add_module(self):
        name = input("Wprowadź nazwę\n>> ")
        image = input("Wprowadź link do obrazu\n>> ")
        description = input("Wprowadź opis\n>> ")
        print("Ile kroków chcesz dodać do zadania?")
        num = input_number(">> ")
        tasks = []
        for i in range(num):
            nam = input("Wprowadź nazwę kroku\n>> ")
            imag = input("Wprowadź link do obrazu\n>> ")
            descript = input("Wprowadź opis\n>> ")
            tasks.append(Task(nam, imag, descript))
        self.available_modules.append(Module(tasks, name, image, description))

    def delete_module(self):
        print("Jakie zadanie chcesz usunąć? (podaj numer od 1 do " + str(len(self.available_modules)) + ")")
        chosen_module = -1
        while chosen_module not in range(1, len(self.available_modules) + 1):
            chosen_module = input_number(">> ")
        chosen_module -= 1
        del self.available_modules[chosen_module]

    def create_module_view(self, clear, chosen_date, order):
        clear()
        print("<< Wciśnij 0 by wrócić\n")
        print("Utwórz nowe zadanie.")
        print("Wybierz zadanie z Twoich zadań:")  # ewentualne katalogi TU
        counter = 1
        for module in self.available_modules:
            print(str(counter) + '.', end = ' ')
            counter += 1
            module.print_module()
        counter = -1
        while order not in range(0, len(self.available_modules) + 1):
            if counter == 0:
                return
            else:
                counter = input_number("\nPamiętaj, że nowe zadania możesz tworzyć w bibliotece zadań.\nWybierz numer od "
                                  "1 do " + str(len(self.available_modules)) + ": ")
        counter -= 1
        self.schedule.add_module(chosen_date, self.available_modules[counter], order)
        return

    def calendar_view(self, clear):
        clear()
        print("\nCo chcesz wyświetlić?  (liczba + enter)")
        print("1. Chcę zobaczyć zadania na dziś")
        print("2. Chcę samemu wybrać datę")
        chosen_date = None
        menu_option = -1
        while menu_option not in range(1, 3):
            menu_option = input_number(">> ")
            if menu_option == 1:
                chosen_date = datetime.date.today()
            if menu_option == 2:
                clear()
                day = input_number("Podaj dzień: ")
                month = input_number("Podaj miesiąc: ")
                year = input_number("Podaj rok: ")
                chosen_date = datetime.date(year, month, day)
        clear()
        print("<< Wciśnij 0 by wrócić\n")
        print("Oto Twój kalendarz! :)\nOto zadania zaplanowane na dziś:\n")
        print("\n" + chosen_date.strftime("%d/%m/%Y"))
        self.schedule.show_tasks_from_date(chosen_date)
        print("\nWybierz aktywność:  (liczba + enter)")
        print("1. Zaplanuj wydarzenie")
        print("2. Przejdź do widoku miesiąca")
        menu_option = -1
        while menu_option not in range(0, 3):
            menu_option = input_number(">> ")
            if menu_option == 1:
                order = 0
                length_l = len(self.schedule.schedule_dict[chosen_date]) if chosen_date in self.schedule.schedule_dict else 0
                if length_l < 1:
                    order = 1
                while order not in range(1, length_l + 2):
                    order = input_number("Podaj, na którym miejscu ma pojawić się nowe zadanie (od 1 do " + str(length_l) + ": ")
                self.create_module_view(clear, chosen_date, order)
                return
            if menu_option == 2:
                pass # TODO
            if menu_option == 0:
                return

    def module_library(self, clear):
        clear()
        print("<< Wciśnij 0 by wrócić\n")
        print("Witaj w bibliotece zadań!\nTutaj możesz tworzyć i edytować zadania.")
        print("Oto Twoje zadania:") # ewentualne katalogi TU
        for module in self.available_modules:
            module.print_module()
        print("\nCo chcesz teraz zrobić?  (liczba + enter)")
        print("1. Edytuj zadanie")
        print("2. Dodaj zadanie")
        print("3. Usuń zadanie")
        menu_option = -1
        while menu_option not in range(0, 4):
            menu_option = input_number(">> ")
            if menu_option == 1:
                self.edit_module()
            if menu_option == 2:
                self.add_module()
            if menu_option == 3:
                self.delete_module()
                pass
            if menu_option == 0:
                return

    def program_loop(self):
        exit_program = True
        clear = lambda: os.system('cls')
        while exit_program is True:
            clear()
            print("Wybierz aktywność:  (liczba + enter)")
            print("1. Kalendarz")
            print("2. Biblioteka nagród")
            print("3. Biblioteka zadań")
            print("4. Podsumowanie")
            print("5. Zakończ program")
            menu_option = input_number(">> ")
            if menu_option == 1:
                self.calendar_view(clear)
            if menu_option == 2:
                clear()
                print("Oto Twój zbiór naklejek.\n\n(W tym miejscu w aplikacji zostaną wyświetlone\nfoldery z naklejkami, "
                      "które mogą zdobywać podopieczni")
                input("\nNaciśnij dowolny klawisz by wrócić.")
                clear()
            if menu_option == 3:
                self.module_library(clear)
            if menu_option == 4:
                clear()
                print("Oto hub podsumowujący.\n\n(W tym miejscu w aplikacji zostaną wyświetlone statystyki,\n"
                      "podsumowanie postępów, zdobyte nagrody i skończone zadania.)")
                input("\nNaciśnij dowolny klawisz by wrócić.")
                clear()
            if menu_option == 5:
                exit_program = False


class ChildInterface:
    def __init__(self, available_modules: list):
        self.schedule = Schedule()
        self.available_modules = available_modules

    def program_loop(self):
        exit_program = True
        while exit_program is True:
            print("Wybierz aktywność:  (liczba+enter)")
            print("1. Utwórz moduł")
            print("2. Dodaj zadanie")
            print("3. Wyświetl zadania")
            print("4. Oznacz zadanie jako wykonane")
            print("5. Zakończ program")
            menu_option = input_number(">> ")
            if menu_option == 5:
                exit_program = False
