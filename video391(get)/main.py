class Employeer():
    def __init__(self, name, salary) -> None:
        self.name = name
        self.__salary = salary

    def get_sallery(self):
        return self.__salary

    def set_sallery(self, amount):
        self.__salary = amount
