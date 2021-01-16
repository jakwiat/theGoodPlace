import datetime
from module import Module
from assigned_module import AssignedModule


class Schedule:
    def __init__(self):
        self.schedule_dict = {}

    def add_module(self, date: datetime.datetime, module: Module):
        self.schedule_dict[date] = AssignedModule(module)

    def show_tasks(self):
        time_list = list(self.schedule_dict.keys())
        time_list.sort()
        for date in time_list:
            date_string = date.strftime("%d/%m/%Y %H:%M")
            print(date_string)
            self.schedule_dict[date].print_module()

    def show_tasks_from_date(self, requested_date: datetime.datetime):
        time_list = list(self.schedule_dict.keys())
        time_list.sort()
        for date in time_list:
            if date.day == requested_date.day and date.month == requested_date.month and date.year == requested_date.year:
                date_string = date.strftime("%d/%m/%Y %H:%M")
                print(date_string)
                self.schedule_dict[date].print_module()

    def show_tasks_from_month(self, requested_date: datetime.datetime):
        time_list = list(self.schedule_dict.keys())
        time_list.sort()
        for date in time_list:
            if date.month == requested_date.month and date.year == requested_date.year:
                date_string = date.strftime("%d/%m/%Y %H:%M")
                print(date_string)
                self.schedule_dict[date].print_module()
