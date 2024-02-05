import sys
from PyQt6.QtWidgets import QApplication, QDialog, QMessageBox, QMainWindow

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
        self.employees = Employees()

    def add(self):
        w = EmployeeAdd(self.employees)
        w.show()
        w.exec()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyForm()
    window.show()
    sys.exit(app.exec())