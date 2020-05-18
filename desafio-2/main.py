

class Department:
    def __init__(self, name, code):
        self.name = name
        self.code = code


class Employee:
    def __init__(self, code, name, salary):
        self.code = code
        self.name = name
        self.salary = salary

    def calc_bonus(self):
        pass

    def get_hours(self):
        pass


class Manager(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)
        self.departament = Department('managers', 1)

    def calc_bonus(self):
        return self.salary * 0.15


class Seller(Manager):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)
        self.departament = Department('sellers', 2)
        self.sales = 0

    def get_hours(self):
        return 6
