class Task:
    # klasa pojedynczego kroku w zadaniu
    def __init__(self, name, image="<obrazek>", description="<opis>"):
        self.name = name
        self.image = image
        self.description = description

    def stringify_task(self):
        # utworzenie informacji tekstowej z obiektu klasy kroku
        string_image = str(self.image) if self.image is not None else ""
        string_description = str(self.description) if self.description is not None else ""
        return str(self.name) + "; " + string_image + "; " + string_description
