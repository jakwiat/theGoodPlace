import datetime
from module import Module


class Schedule:
    def __init__(self):
        self.schedule_dict = {}

    def add_module(self, date: datetime.datetime, module: Module):
        self.schedule_dict[date] = module

    def show_tasks(self):
        time_list = list(self.schedule_dict.keys())
        time_list.sort()
        for date in time_list:
            date_string = date.strftime("%d/%m/%Y %H:%M")
            print(date_string)
            self.schedule_dict[date].print_module()