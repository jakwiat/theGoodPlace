from task import Task
from module import Module

if __name__ == "__main__":
    print("Welcome to Time Organizer app!! Hope you feeling great :)")
    print()
    task = Task("Wash your hands")
    module = Module([task, Task("Eat dinner")], "Dinner", "image_url", "Short description")
    module.print_module()
