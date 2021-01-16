import datetime
from task import Task
from module import Module
from schedule import Schedule
from interfaces import ParentInterface, ChildInterface


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

    print("Child (c) or parent (p)?")
    user = input(">> ")
    if user == 'c':
        interface = ChildInterface(schedul)
    elif user == 'p':
        interface = ParentInterface(schedul)
    interface.program_loop()

