from module import Module
from award import Award


class AssignedModule:
    # instancja modułu zaplanowana w konkretnym terminie i zawierająca informacje o stanie wykonania
    def __init__(self, module: Module):
        self.module = module
        self.how_many_tasks = len(module.tasks_list)
        self.which_task_to_do = 0
        self.is_done = False
        self.award = None

    def print_module(self):
        # drukowanie informacji o szczegółach modułu
        self.module.print_module()

    def print_module_child(self, param=""):
        # drukowanie tytułu i ewentualnego stanu wykonania w ramce symulującej geometrię aplikacji mobilnej
        print("+---------------------------------")
        if self.is_done:
            print("|\n|  " + param + " " + self.module.name + " - ZROBIONE")
        else:
            print("|\n|  " + param + " " + self.module.name)
        print("|")

    def make_progress(self):
        self.which_task_to_do += 1
        if self.which_task_to_do == self.how_many_tasks:
            self.is_done = True
            return True
        return False
