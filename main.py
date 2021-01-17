import datetime
from task import Task
from module import Module
from award import Award
from schedule import Schedule
from interfaces import ParentInterface, ChildInterface


if __name__ == "__main__":

    # create default awards
    award_list = [Award("Złoty medal."), Award("Świetna robota!"), Award("Brawo :)"), Award("Oby tak dalej")]

    # create default modules
    lazienka = Task("Idę do łazienki.")
    wez = Task("Wyciągam szczoteczkę i pastę.")
    naloz = Task("Nakładam pastę na szczoteczkę.")
    czysc_z = Task("Szoruję zęby")
    plucz = Task("Płuczę usta.")
    plucz2 = Task("Płuczę szczoteczkę.")
    odloz = Task("Odkładam szczoteczkę i pastę.")
    wytrzyj = Task("Wycieram buzię i ręce.")
    lista = Task("Robię listę zakupów.")
    buty_on = Task("Ubieram buty.")
    kurtka_on = Task("Ubieram kurtkę.")
    klucz = Task("Biorę klucze.")
    drzwi = Task("Zamykam drzwi.")
    sklep = Task("Ide do sklepu")
    kupuje = Task("Kupuję mleko.")
    place = Task("Płacę.")
    wracam = Task("Wracam do domu.")
    kurtka_off = Task("Zdejmuję kurtkę.")
    buty_off = Task("Zdejmuję buty.")
    pokoj = Task("Idę do pokoju.")
    koldra = Task("Układam kołdrę.")
    poduszka = Task("Układam poduszkę.")
    pluszak = Task("Ustawiam równo pluszaki.")
    koc = Task("Układam kocyk.")
    kuchnia = Task("Idę do kuchni.")
    zmywarka1 = Task("Otwieram zmywarkę.")
    zmywarka2 = Task("Wkładam szklanki do szafki.")
    zmywarka3 = Task("Wkładam sztućce do szuflady.")
    zmywarka4 = Task("Wkładamy garnki do szafki.")
    zmywarka5 = Task("Wkładam miski i talerze do szafki.")
    zmywarka6 = Task("Zamykam zmywarkę.")
    chleb = Task("Wyjmuję chleb.")
    maslo = Task("Smaruję chleb masłem.")
    ser = Task("Na chleb kładę ser.")
    pomidor = Task("Na ser kładę pomidor.")
    jem = Task("Jem kanapkę.")

    default_modules_list = []
    default_modules_list.append(
        Module([kuchnia, chleb, maslo, ser, pomidor, jem],
               "Robię kanapkę", "image_url", "DEMO: Podstawowe zadanie robienia kanapki z serem i pomidorem."))
    default_modules_list.append(
        Module([lazienka, wez, czysc_z, plucz, plucz2, odloz, wytrzyj], "Myję zęby", "image_url",
               "DEMO: Podstawowe zadanie mycia zębów."))
    default_modules_list.append(
        Module([kuchnia, zmywarka1, zmywarka2, zmywarka3, zmywarka4, zmywarka5, zmywarka6], "Rozpakowuję zmywarkę",
               "image_url", "DEMO: Podstawowe zadanie wypakowania zmywarki (garnki, talerze, miski, sztućce)."))
    default_modules_list.append(
        Module([pokoj, koldra, poduszka, pluszak, koc], "Ścielę łóżko", "image_url",
               "DEMO: Podstawowe zadanie ścielenia łóżka."))
    default_modules_list.append(
        Module([lista, buty_on, kurtka_on, klucz, drzwi, sklep, kupuje, place, wracam, kurtka_off, buty_off],
               "Wyjście do sklepu", "image_url", "DEMO: Podstawowe zadanie wyjścia do sklepu."))

    Przyklad = Schedule(award_list)
    Przyklad.add_module(datetime.date(2021, 1, 17), default_modules_list[0], 1)
    Przyklad.add_module(datetime.date(2022, 5, 17), default_modules_list[1], 1)
    Przyklad.add_module(datetime.date(2021, 7, 17), default_modules_list[2], 1)
    Przyklad.add_module(datetime.date(2021, 1, 17), default_modules_list[3], 2)
    Przyklad.add_module(datetime.date(2021, 1, 17), default_modules_list[4], 1)
    Przyklad.add_module(datetime.date(2021, 1, 19), default_modules_list[4], 1)


    for i in range(11):
        Przyklad.make_progress()

    # start of app
    print("Witaj w aplikacji Codzienne Wyzwania! Mamy nadzieję, że masz się dobrze :)")
    print()
    print("Czy aplikacja ma przyjąć tryb dziecka (d) czy rodzica (r)?")
    user = input(">> ")
    if user == 'd':
        interface = ChildInterface(default_modules_list, award_list)
    elif user == 'r':
        interface = ParentInterface(default_modules_list, award_list)
    interface.schedule = Przyklad
    interface.program_loop()

