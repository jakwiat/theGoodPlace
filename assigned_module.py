from module import Module


class AssignedModule:
    def __init__(self, module: Module):
        self.module = module
        self.how_many_tasks = len(module.tasks_list)
        self.which_task_to_do = 0
        self.is_done = False

    def print_module(self):
        self.module.print_module()

    def make_progress(self):
        self.which_task_to_do += 1
        if self.which_task_to_do == self.how_many_tasks:
            self.is_done = True
