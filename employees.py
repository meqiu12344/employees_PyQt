from employee import Employee


class Employees:

    def __init__(self):
        self.list = []

    def add(self, emp: Employee):
        self.list.append(emp)

    def remove(self, emp: Employee):
        self.list.remove(emp)

    def get(self, id=None, name=None, surname=None, pesel=None):
