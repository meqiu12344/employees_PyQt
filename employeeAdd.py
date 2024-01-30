from PyQt6.QtWidgets import QDialog

from employee import Employee
from employeeView import Ui_EmployeeView


class EmployeeAdd(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_EmployeeView()
        self.ui.setupUi(self)
        self.ui.saveButton.clicked.connect(self.save)

    def save(self):
        name = self.ui.nameValue.text()
        secondName = self.ui.secondNameValue.text()
        pesel = self.ui.peselValue.text()
        contract = self.ui.typeCheckBox.isChecked()
        phone = self.ui.PhoneValue.text()

        emp = Employee(secondName, name, phone, pesel, contract)
