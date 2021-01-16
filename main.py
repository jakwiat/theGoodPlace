from task import Task
from module import Module

if __name__ == "__main__":
    print("Welcome to Time Organizer app!! Hope you feeling great :)")
    task = Task("Wash your hands")
    task.print_task()
    module = Module([task, Task("Eat dinner")], "Dinner")
    module.print_module()
