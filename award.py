class Award:
    # klasa nagrody - naklejki, otrzymywanej za ukończone zadanie (AssignedModule),
    # zawierająca miejsce na inforamcję graficzną - obrazek
    def __init__(self, name, image="<obrazek>"):
        self.name = name
        self.image = image

