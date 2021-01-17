import datetime
import random
from module import Module
from assigned_module import AssignedModule
from award import Award


class Schedule:
    def __init__(self, awards_list: list = None):
        self.schedule_dict = {}
        self.today = datetime.date.today()
        self.current_module = None
        self.awards_list = awards_list if awards_list is not None else [Award("Order 1"), Award("Order 2")]

    def add_module(self, date: datetime.date, module: Module, place: int):
        if date in self.schedule_dict:
            self.schedule_dict[date].insert(place - 1, AssignedModule(module))
        else:
            self.schedule_dict[date] = [AssignedModule(module)]
        if self.today == date:
            if self.current_module is None:
                self.current_module = 0

    def show_tasks(self):
        time_list = list(self.schedule_dict.keys())
        time_list.sort()
        for date in time_list:
            for task in range(len(self.schedule_dict[date])):
                date_string = date.strftime("%d/%m/%Y")
                print(date_string, task + 1, sep="  -  ", end=". ")
                self.schedule_dict[date][task].print_module()

    def show_tasks_from_date(self, requested_date: datetime.date):
        time_list = list(self.schedule_dict.keys())
        time_list.sort()
        for date in time_list:
            if date.day == requested_date.day and date.month == requested_date.month and date.year == requested_date.year:
                for task in range(len(self.schedule_dict[date])):
                    self.schedule_dict[date][task].print_module_child(str(task + 1) + ".")
                return

    def show_tasks_from_month(self, requested_date: datetime.date):
        time_list = list(self.schedule_dict.keys())
        time_list.sort()
        for date in time_list:
            if date.month == requested_date.month and date.year == requested_date.year:
                for task in range(len(self.schedule_dict[date])):
                    date_string = date.strftime("%d/%m/%Y")
                    print(date_string, task + 1, sep="  -  ", end=". ")
                    self.schedule_dict[date][task].print_module()

    def make_progress(self):
        if self.current_module is not None:
            is_done = self.schedule_dict[self.today][self.current_module].make_progress()
            if is_done is True:
                self.schedule_dict[self.today][self.current_module].award = random.choice(self.awards_list)
                if self.current_module + 1 < len(self.schedule_dict[self.today]):
                    self.current_module += 1
                else:
                    self.current_module = None

    def update_today(self, today: datetime.date):
        self.today = today
        if today in self.schedule_dict:
            self.current_module = 0
        else:
            self.current_module = None

    def get_done_modules(self):
        done_modules = {}
        time_list = list(self.schedule_dict.keys())
        time_list.sort()
        for date in time_list:
            if date < self.today:
                done_modules[date] = []
                for modules in self.schedule_dict[date]:
                    done_modules[date].append(modules)
            elif date == self.today:
                if self.current_module is None or self.current_module != 0:
                    done_modules[date] = []
                    for modules in self.schedule_dict[date]:
                        if modules.is_done is True:
                            done_modules[date].append(modules)
        return done_modules
