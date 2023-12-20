import sys
from PyQt6.QtWidgets import QApplication, QDialog, QMessageBox
import re
from layout import Ui_Dialog


class Myform(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.isValid = True
        self.show()
        self.ui.saveButton.clicked.connect(self.saveToComboBox)
        self.ui.saveToFileButton.clicked.connect(self.saveToFile)

    def allert(self):
        self.isValid = False
        alert = QMessageBox()
        alert.setWindowTitle("Błąd")
        alert.setInformativeText("Nieprawidłowe dane spróbój ponownie")
        alert.setStandardButtons(QMessageBox.StandardButton.Ok)
        alert.exec()

    def validation(self):
        suma = 0
        wagi = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
        name = self.ui.nameValue.text()
        secondName = self.ui.secondNameValue.text()
        phoneNumber = self.ui.PhoneValue.text()
        peselNumber = self.ui.peselValue.text()
        if len(name) == 0 or len(secondName) == 0:
            self.allert()
            return
        if len(phoneNumber) == 9 and len(peselNumber) == 11:
            try:
                int(phoneNumber)
                int(peselNumber)
                self.isValid = True
            except ValueError:
                self.allert()
                return
        else:
            self.allert()
            return

        for i in range(11):
            x = wagi[i] * int(peselNumber[i])
            suma += x
        if suma < 10:
            cyfraKontrolna = suma
        else:
            cyfraKontrolna = suma % 10

        if cyfraKontrolna != int(peselNumber[10]):
            self.allert()
        else:
            self.isValid = True

    def saveToFile(self):
        self.validation()
        if self.isValid:
            name = self.ui.nameValue.text()
            secondName = self.ui.secondNameValue.text()
            phoneNumber = self.ui.PhoneValue.text()
            peselNumber = self.ui.peselValue.text()
            checkBoxValue = self.ui.typeCheckBox.isChecked()
            if checkBoxValue:
                data_to_save = f"Imie: {name}\nNazwisko: {secondName}\nNumer telefonu: {phoneNumber}\nPESEL: {peselNumber}\nCzy Umowa o prace: TAK\n"
            else:
                data_to_save = f"Imie: {name}\nNazwisko: {secondName}\nNumer telefonu: {phoneNumber}\nPESEL: {peselNumber}\nCzy Umowa o prace: NIE\n"
            filename = "imie_nazwisko.txt"
            with open(filename,'a') as plik:
                plik.write(data_to_save)

    def saveToComboBox(self):
        self.validation()
        if self.isValid:
            name = self.ui.nameValue.text()
            secondName = self.ui.secondNameValue.text()
            data_to_save = f"{name} {secondName}"
            self.ui.lista.addItem(data_to_save)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Myform()
    window.show()
    sys.exit(app.exec())