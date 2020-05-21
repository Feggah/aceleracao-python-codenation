from abc import ABC, abstractmethod


class Department:
    def __init__(self, name, code):
        self.__name = name
        self.__code = code

    # Getter e setter para os atributos de Department
    def get_name(self):
        return self.__name

    def set_name(self, dep):
        self.__name = dep


# Declarando a classe Employee como abstrata
class Employee(ABC):
    @abstractmethod
    def __init__(self, code, name, salary):
        self.__code = code
        self.__name = name
        self._salary = salary
        self._hours = 8

    @abstractmethod
    def calc_bonus(self):
        pass

    @abstractmethod
    def get_hours(self):
        pass


class Manager(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)
        self.__departament = Department('managers', 1)

    # Getters e setters para os atributos de Manager
    def get_departament(self):
        return self.__departament.get_name()

    def set_department(self, dep):
        self.__departament.set_name(dep)

    def get_salary(self):
        return self._salary

    # Implementação dos contratos da classe-pai
    def get_hours(self):
        return self._hours

    def calc_bonus(self):
        return self.get_salary() * 0.15


class Seller(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)
        self.__departament = Department('sellers', 2)
        self.__sales = 0

    # Getters e setters para os atributos da classe Seller
    def get_sales(self):
        return self.__sales

    def put_sales(self, sales):
        self.__sales += sales

    def get_departament(self):
        return self.__departament.get_name()

    def get_salary(self):
        return self._salary

    # Implementação dos contratos da classe-pai
    def get_hours(self):
        return self._hours

    def calc_bonus(self):
        return self.get_sales() * 0.15
