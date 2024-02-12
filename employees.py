import json
from json import JSONDecodeError

from employee import Employee


class Employees:
    def __init__(self):
        self.list = []
        self.init_list()

    def init_list(self):
        try:
            with open('pracownicy.json', 'r') as file:
                data = json.load(file)

            new_data = json.loads(data)

            for pracownik in new_data:
                emp = Employee(pracownik['surname'], pracownik['name'], pracownik['phoneNumber'], pracownik['pesel'], pracownik['contract'])
                self.add(emp)
                
        except (FileNotFoundError, JSONDecodeError) as e:
            return 0

    def add(self, emp: Employee):
        print('cos')
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

    def get_list(self) -> list:
        return [e.__str__() for e in self.list]
