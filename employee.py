class Employee:

    next_id = 0

    def __init__(self, surname: str, name: str, phoneNumber: str, pesel: str):
        self.id = self.next_id
        self.next_id += 1
        self.name = name
        self.surname = surname
        self.phoneNumber = phoneNumber
        if len(pesel) == 11 and self.validatePesel(pesel):
            self.pesel = pesel
        else:
            raise ValueError

    def validatePesel(self, pesel: str):
        sum = 0
        weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
        for i in range(10):
            x = weights[i] * int(pesel[i])
            sum += x
        controlNumber = 0
        sum = sum % 10
        if sum == 0:
            controlNumber = sum
        else:
            controlNumber = 10 - sum

        if controlNumber != int(pesel[10]):
            return False
        else:
            return True



