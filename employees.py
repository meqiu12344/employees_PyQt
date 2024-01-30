from employee import Employee


class Employees:

    def __init__(self):
        self.list = []

    def add(self, emp: Employee):
        self.list.append(emp)

    def remove(self, emp: Employee):
        self.list.remove(emp)

    def get(self, id=None, name=None, surname=None, pesel=None):
        result = []
        for emp in self.list:
            if emp.id == id:
                result.append(emp)
            elif emp.name == name:
                result.append(emp)
            elif emp.surname == surname:
                result.append(emp)
            elif emp.pesel == pesel:
                result.append(emp)

        return result
