import datetime
import random
from module import Module
from assigned_module import AssignedModule
from award import Award


class Schedule:
    # klasa planu
    def __init__(self, awards_list: list = None):
        self.schedule_dict = {}
        self.today = datetime.date.today()
        self.current_module = None
        self.awards_list = awards_list if awards_list is not None else [Award("Order 1"), Award("Order 2")]

    def add_module(self, date: datetime.date, module: Module, place: int):
        # funkcja tworząca nowy moduł ("duże" zadanie)
        if date in self.schedule_dict:
            self.schedule_dict[date].insert(place - 1, AssignedModule(module))
        else:
            self.schedule_dict[date] = [AssignedModule(module)]
        if self.today == date:
            if self.current_module is None:
                self.current_module = 0

    def show_tasks(self):
        # wypisanie wszystkich modułów (zadań) i przypisanych im kroków
        time_list = list(self.schedule_dict.keys())
        time_list.sort()
        for date in time_list:
            for module in range(len(self.schedule_dict[date])):
                date_string = date.strftime("%d/%m/%Y")
                print(date_string, module + 1, sep="  -  ", end=". ")
                self.schedule_dict[date][module].print_module()

    def show_tasks_from_date(self, requested_date: datetime.date):
        # wypisywanie wszystkich zadań (modułów) z danej daty
        time_list = list(self.schedule_dict.keys())
        time_list.sort()
        for date in time_list:
            if date.day == requested_date.day and date.month == requested_date.month and date.year == requested_date.year:
                for module in range(len(self.schedule_dict[date])):
                    self.schedule_dict[date][module].print_module_child(str(module + 1) + ".")
                return

    def show_tasks_from_month(self, requested_date: datetime.date):
        # wypisywanie wszysktich zadań (modułów) z danego miesiąca
        time_list = list(self.schedule_dict.keys())
        time_list.sort()
        for date in time_list:
            if date.month == requested_date.month and date.year == requested_date.year:
                print(date.strftime("%d/%m/%Y") + "")
                for module in range(len(self.schedule_dict[date])):
                    self.schedule_dict[date][module].print_module_child(str(module + 1) + ".")
                print("+---------------------------------\n")

    def make_progress(self):
        # zarejestrowanie kolejnego wykonanego kroku w zadaniu - True jeśli był to krok ostatni
        if self.current_module is not None:
            is_done = self.schedule_dict[self.today][self.current_module].make_progress()
            if is_done is True:
                self.schedule_dict[self.today][self.current_module].award = random.choice(self.awards_list)
                if self.current_module + 1 < len(self.schedule_dict[self.today]):
                    self.current_module += 1
                else:
                    self.current_module = None
                return True
            else:
                return False

    def update_today(self, today: datetime.date):
        # ustawienie dzisiejszej daty
        self.today = today
        if today in self.schedule_dict:
            self.current_module = 0
        else:
            self.current_module = None

    def get_done_modules(self):
        # zwraca ukończone moduły (zadania)
        done_modules = {}
        time_list = list(self.schedule_dict.keys())
        time_list.sort()
        for date in time_list:
            if date < self.today:
                done_modules[date] = []
                for module in self.schedule_dict[date]:
                    done_modules[date].append(module)
            elif date == self.today:
                if self.current_module is None or self.current_module != 0:
                    done_modules[date] = []
                    for module in self.schedule_dict[date]:
                        if module.is_done is True:
                            done_modules[date].append(module)
        return done_modules
