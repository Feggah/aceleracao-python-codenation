

class Department:
    def __init__(self, name, code):
        self.name = name
        self.code = code


class Employee:
    def __init__(self, code, name, salary):
        if type(self) == Employee:
            raise TypeError("Classe employee não deve ser instanciada diretamente.")
        self.code = code
        self.name = name
        self.salary = salary
        self.hours = 8

    def calc_bonus(self):
        raise NotImplementedError

    def get_hours(self):
        raise NotImplementedError


class Manager(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)
        self.__departament = Department('managers', 1)

    def calc_bonus(self):
        return self.salary * 0.15

    def get_hours(self):
        return self.hours

    def get_departament(self):
        return self.__departament.name

    def set_department(self, dep):
        self.__departament.name = dep


class Seller(Manager):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)
        self.__departament = Department('sellers', 2)
        self.__sales = 0

    def get_hours(self):
        return self.hours

    def calc_bonus(self):
        return self.__sales * 0.15

    def get_sales(self):
        return self.__sales

    def put_sales(self, sales):
        self.__sales += sales

    def get_departament(self):
        return self.__departament.name
