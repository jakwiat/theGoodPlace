from task import Task


class Module(Task):
    def __init__(self, tasks_list, name, image="<obrazek>", description="<opis>"):
        Task.__init__(self, name, image, description)
        self.tasks_list = tasks_list

    def print_module(self):
        print(self.name, self.image, self.description, sep="; ")
        for task in self.tasks_list:
            print(" - ", task.stringify_task())
