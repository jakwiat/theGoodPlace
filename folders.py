from module import Module
from award import Award


class ModuleFolder:
    # klasa kategorii, na które docelowo podzielone zostaną duże zadania (Modules)
    def __init__(self, name: str, modules_list: list):
        self.name = name
        self.modules_list = modules_list


class AwardFolder:
    # klasa kategorii, na które docelowo podzielone zostaną nagrody-naklejki zdobyte za wykonane zadania (Awards)
    def __init__(self, name: str, award_list: list):
        self.name = name
        self.award_list = award_list
