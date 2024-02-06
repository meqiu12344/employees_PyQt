import json
import sys
from PyQt6.QtWidgets import QApplication, QDialog, QMessageBox, QMainWindow

from employee import EmployeeEncoder
from employeeAdd import EmployeeAdd
from employees import Employees
from menu import Ui_Menu


class MyForm(QDialog):



    def __init__(self):
        super().__init__()
        self.ui = Ui_Menu()
        self.ui.setupUi(self)
        self.show()
        self.ui.add.clicked.connect(self.add)
        self.ui.save.clicked.connect(self.save)
        self.employees = Employees()

    def add(self):
        w = EmployeeAdd(self.employees)
        w.show()
        w.exec()
        self.ui.comboBox.clear()
        self.ui.comboBox.addItems(self.employees.get_list())

    def save(self):
        json_object = json.dumps(self.employees.list, cls=EmployeeEncoder)
        print(json_object)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyForm()
    window.show()
    sys.exit(app.exec())