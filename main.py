import datetime
from task import Task
from module import Module
from schedule import Schedule

if __name__ == "__main__":
    print("Welcome to Time Organizer app!! Hope you feeling great :)")
    print()
    task = Task("Wash your hands")
    module = Module([task, Task("Eat dinner")], "Dinner", "image_url", "Short description")
    module.print_module()

    x = datetime.datetime.now()

    schedul = Schedule()
    schedul.add_module(datetime.datetime(2020, 5, 17, 12), module)
    schedul.add_module(datetime.datetime(2010, 5, 17, 13), module)
    schedul.add_module(datetime.datetime(2020, 7, 17, 14), module)
    schedul.add_module(datetime.datetime(2020, 5, 12, 8), module)
    schedul.show_tasks()

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
