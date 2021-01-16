from task import Task


class Module(Task):
    def __init__(self, tasks_list, name, image=None, description=None):
        Task.__init__(self, name, image, description)
        self.tasks_list = tasks_list
        self.is_done = False

    def print_module(self):
        print(self.name, self.image, self.description, sep="; ")
        for task in self.tasks_list:
            print(" - ", task.stringify_task())
