import datetime
from module import Module
from assigned_module import AssignedModule


class Schedule:
    def __init__(self):
        self.schedule_dict = {}
        self.today = datetime.datetime.now()
        self.current_task_key = None

    def add_module(self, date: datetime.datetime, module: Module, place: int):
        if date in self.schedule_dict:
            self.schedule_dict[date].insert(AssignedModule(module), place - 1)
        else:
            self.schedule_dict[date] = [AssignedModule(module)]
        if self.today == date:
            if self.current_task_key is None:
                self.current_task_key = 0

    def show_tasks(self):
        time_list = list(self.schedule_dict.keys())
        time_list.sort()
        for date in time_list:
            for task in self.schedule_dict[date]:
                date_string = date.strftime("%d/%m/%Y")
                print(date_string, task, sep="  -  ", end=". ")
                self.schedule_dict[date][task].print_module()

    def show_tasks_from_date(self, requested_date: datetime.datetime):
        time_list = list(self.schedule_dict.keys())
        time_list.sort()
        for date in time_list:
            if date.day == requested_date.day and date.month == requested_date.month and date.year == requested_date.year:
                for task in self.schedule_dict[date]:
                    date_string = date.strftime("%d/%m/%Y")
                    print(date_string, task, sep="  -  ", end=". ")
                    self.schedule_dict[date][task].print_module()
                return

    def show_tasks_from_month(self, requested_date: datetime.datetime):
        time_list = list(self.schedule_dict.keys())
        time_list.sort()
        for date in time_list:
            if date.month == requested_date.month and date.year == requested_date.year:
                for task in self.schedule_dict[date]:
                    date_string = date.strftime("%d/%m/%Y")
                    print(date_string, task, sep="  -  ", end=". ")
                    self.schedule_dict[date][task].print_module()

    def make_progress(self):
        if self.current_task_key is not None:
            is_done = self.schedule_dict[self.today][self.current_task_key].make_progress()
            if is_done is True:
                if self.current_task_key + 1 < len(self.schedule_dict[self.today]):
                    self.current_task_key += 1
                else:
                    self.current_task_key = None

    def update_today(self, today: datetime.datetime):
        self.today = today
        if today in self.schedule_dict:
            self.current_task_key = 0
        else:
            self.current_task_key = None
