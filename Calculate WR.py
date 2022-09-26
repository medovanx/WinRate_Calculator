import sys
from PyQt6.QtWidgets import QLineEdit, QLabel, QApplication, QWidget
from PyQt6 import QtGui, QtCore
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(300, 260)
        self.setWindowTitle("Calculate WR")
        self.setWindowIcon(QtGui.QIcon("M:\\Mohamed\\Programming\\Calculate WR\\icon.ico"))

        self.description = QLabel("  Calculate how many matches you need to win\n                  to reach a certain winrate.", self)
        self.description.setStyleSheet("""font-weight: bold;""")
        self.description.move(0, 5)

        self.matches_label = QLabel("Matches played:", self)
        self.matches_label.move(100, 50)
        self.matches = QLineEdit(self)
        self.matches.setPlaceholderText("Enter matches.")
        self.matches.move(60, 70)
        self.matches.resize(180, 25)
        self.matches.setStyleSheet("""font-weight: bold; border: 2px solid green; font-size: 13px; border-radius: 6px;""")
        self.matches.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.matches.returnPressed.connect(self.func)

        self.winrate_label = QLabel("Winrate:", self)
        self.winrate_label.move(125, 100)
        self.winrate = QLineEdit(self)
        self.winrate.setPlaceholderText("Enter winrate.")      
        self.winrate.move(60, 120)
        self.winrate.resize(180, 25)
        self.winrate.setStyleSheet("""font-weight: bold; border: 2px solid green; font-size: 13px; border-radius: 6px;""")
        self.winrate.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.winrate.returnPressed.connect(self.func)

        self.expected_wr_label = QLabel("Expected WR:", self)
        self.expected_wr_label.move(115, 150)
        self.expected_wr = QLineEdit(self)
        self.expected_wr.setPlaceholderText("Enter expected winrate.")
        self.expected_wr.move(60, 170)
        self.expected_wr.resize(180, 25)
        self.expected_wr.setStyleSheet("""font-weight: bold; border: 2px solid green; font-size: 13px; border-radius: 6px;""")
        self.expected_wr.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.expected_wr.returnPressed.connect(self.func)

        self.result= QLabel(self)
        self.result.resize(200, 25)
        self.result.move(95, 200)
        self.result.setStyleSheet("""font-weight: bold;""")
        self.show

        self.author = QLabel("Created by: Mohamed Darwesh (@medovanx)", self)
        self.author.move(10, 240)
        self.author.setStyleSheet("""font-weight: bold; font-size: 12px;""")
        self.show()



    def func(self):
        try:
            from sympy import symbols, solve
            matches = int(self.matches.text())
            winrate = float(self.winrate.text())/100
            expected_wr = float(self.expected_wr.text())/100
            x = symbols('x')
            result = (((matches * winrate)) + x ) / (matches + x) - expected_wr    
            result = [float(i) for i in solve(result)][0]
            self.result.setText(f"{str(round(result, 2))} matches")
            self.result.setStyleSheet("""font-weight: bold; color: green;""")
        except ValueError:
            self.result.setText("Enter valid values.")
            self.result.setStyleSheet("""color: red; font-weight: bold;""")
        

app = QApplication([])
window = Window()
window.show()
sys.exit(app.exec())      
"""
x = symbols('x')

matches = int(input("Enter total matches: "))
winrate = float(input("Enter Win Rate: "))/100
expected_wr = float(input("Enter Expected WR: "))/100
      
result = (((matches * winrate)) + x ) / (matches + x) - expected_wr

print(solve(result))"""