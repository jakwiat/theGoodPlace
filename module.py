from task import Task


class Module:
    def __init__(self, tasks_list, name):
        self.name = name
        self.tasks_list = tasks_list

    def print_module(self):
        print(self.name)
        for task in self.tasks_list:
            print(" - ", task.name)
