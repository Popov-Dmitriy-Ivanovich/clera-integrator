from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget,QPushButton, QMessageBox,QDialog
from PyQt6.QtCore import QSize, Qt
import sys
from draw_funcitons import Graphic, Dif_Graphic
from math_functions import definite

from GUI_functions import Read_Data
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(QSize(350, 150))
        self.setStyleSheet("background-color: #aab3a5;")
        self.label= QLabel("The value of definite integral will be here")
        self.setWindowTitle("clera-integrator")
        self.input = QLineEdit("enter path to input file")
        self.dlg = QMessageBox(self)
        self.diff_button = QPushButton("show differintiated function")
        self.val_button = QPushButton("show value of definite integral")
        self.indef_button = QPushButton("show integrated funciton")

        self.diff_button.clicked.connect(self.show_differintiated)        
        self.val_button.clicked.connect(self.show_value)        
        self.indef_button.clicked.connect(self.show_integrated)
        
        self.dlg.setWindowTitle("exception")
        self.dlg.setText("Invalid name of file")
        #self.dlg.setStyleSheet("background-clolor:#FFFFFF")
        self.input.setStyleSheet("background-color: #d9cebe;border:0px;border-radius: 3px;")   
        
        self.diff_button.setStyleSheet("background-color: #d9cebe;border:0px;min-height: 25px;border-radius: 4px;")
        self.val_button.setStyleSheet("background-color: #d9cebe;border:0px;min-height: 25px;border-radius: 4px;")
        self.indef_button.setStyleSheet("background-color: #d9cebe;border:0px;min-height: 25px;border-radius: 4px;")
        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.diff_button)
        layout.addWidget(self.val_button)
        layout.addWidget(self.indef_button)
        layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def show_differintiated(self):
        path=self.input.text()
        data=Read_Data(path)
        if not data['FlagInvFile']:
            Dif_Graphic (data["InitialFuncY"], data["FuncX"], data["eps"],data["C"])
        else:
            self.dlg.show()

    def show_integrated(self):
        path=self.input.text()
        data=Read_Data(path)
        if not data['FlagInvFile']:
            Graphic (data["InitialFuncY"], data["FuncX"], data["eps"],data["C"])
        else:
            self.dlg.show()

    def show_value(self):
        path=self.input.text()
        data=Read_Data(path)
        if not data['FlagInvFile']:
           self.label.setText("value is:"+ str(definite(data["InitialFuncY"],data["eps"])))
        else:
            self.dlg.show()
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()