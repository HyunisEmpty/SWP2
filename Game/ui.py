import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication, QLabel,
    QComboBox, QTextEdit, QLineEdit)
from PyQt5.QtCore import Qt

class Game(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.showGame()
        self.text_case = ""

    def initUI(self):
        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Game')

        self.txtResult = QTextEdit()

        # QPushButtons 통해 각 버튼을 정의하며 라벨에 맞는 버튼명으로 변수명을 정의한다.
        label_Name = QLabel('입력: ', self)

        line_Name = QLineEdit("", self)

        button_Add = QPushButton("입력", self)

        button_Add.clicked.connect(lambda: self.doScoreDb(line_Name.text()))

        # 새번째 QHBoxLayout, 각 버튼들이 있는 줄이다.
        horizontal_box3 = QHBoxLayout()

        horizontal_box3.addStretch(0)
        horizontal_box3.addWidget(label_Name)
        horizontal_box3.addWidget(line_Name)
        horizontal_box3.addWidget(button_Add)

        vertical_box = QVBoxLayout()
        vertical_box.addWidget(self.txtResult)
        vertical_box.addLayout(horizontal_box3)

        self.setLayout(vertical_box)
        self.show()

    def showGame(self, hp = -1, day = -1, event = "test_case"):
        hpText = "현재 가지고 있는 식량은 " + str(hp) + "개입니다. 현재 " + str(day) + "일째입니다."
        self.txtResult.setText("")

        # 게임이 처음 시작하는 부분.
        if event == "first_start":
            self.txtResult.append(hpText)
            resultText = """여러분은 핵전쟁이후 방공호에 들어왔습니다.
식량이 0이 된면 여러분은 죽게 됩니다.
앞으로의 선택을 통해 최대한 오래동안 생존하세요.
yes를 입력해서 게임을 시작해주세요"""
            self.txtResult.append(resultText)
            if self.text_case == "yes":
                self.txtResult.append("올바른 입력확인")
            else:
                self.txtResult.append("다시 입력 해주세요")

    def doScoreDb(self, text):
        self.text_case = text

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Game()
    sys.exit(app.exec_())