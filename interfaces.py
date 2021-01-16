class ParentInterface:
    def __init__(self, schedule):
        self.schedule = schedule

    def program_loop(self):
        exit_program = True
        while exit_program is True:
            print("Wybierz aktywność:  (liczba+enter)")
            print("1. Utwórz moduł")
            print("2. Dodaj zadanie")
            print("3. Wyświetl zadania")
            print("4. Oznacz zadanie jako wykonane")
            print("5. Zakończ program")
            menu_option = int(input(">> "))
            if menu_option == 5:
                exit_program = False


class ChildInterface:
    def __init__(self, schedule):
        self.schedule = schedule

    def program_loop(self):
        exit_program = True
        while exit_program is True:
            print("Wybierz aktywność:  (liczba+enter)")
            print("1. Utwórz moduł")
            print("2. Dodaj zadanie")
            print("3. Wyświetl zadania")
            print("4. Oznacz zadanie jako wykonane")
            print("5. Zakończ program")
            menu_option = int(input(">> "))
            if menu_option == 5:
                exit_program = False
