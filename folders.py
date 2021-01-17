from module import Module
from award import Award


class ModuleFolder:
    def __init__(self, name: str, modules_list: list):
        self.name = name
        self.modules_list = modules_list


class AwardFolder:
    def __init__(self, name: str, award_list: list):
        self.name = name
        self.award_list = award_list
