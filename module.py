from task import Task


class Module(Task):
    # klasa modułu ("dużego" zadania)
    def __init__(self, tasks_list, name, image="<obrazek>", description="<opis>"):
        Task.__init__(self, name, image, description)
        self.tasks_list = tasks_list

    def print_module(self):
        # drukowanie szczegółów (zastosowanie - biblioteka)
        print(self.name, self.image, self.description, sep="; ")
        for task in self.tasks_list:
            print(" - ", task.stringify_task())

    def print_module_child(self, param=""):
        # drukowanie tytułu w ramce symulującej geometrię aplikacji mobilnej
        print("\n+---------------------------------")
        print("|\n|  " + param + " " + self.name)
        print("|")
