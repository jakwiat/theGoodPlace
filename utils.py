def input_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Proszę, wpisz liczbę :)")
