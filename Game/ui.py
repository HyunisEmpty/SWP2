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

    def initUI(self):
        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Game')

        self.txtResult = QTextEdit()


        # QPushButtons 통해 각 버튼을 정의하며 라벨에 맞는 버튼명으로 변수명을 정의한다.
        button_Add = QPushButton("네", self)
        button_Del = QPushButton("아니요", self)
        button_Find = QPushButton("날짜넘기기", self)

        # 새번째 QHBoxLayout, 각 버튼들이 있는 줄이다.
        horizontal_box3 = QHBoxLayout()

        horizontal_box3.addStretch(0)
        horizontal_box3.addWidget(button_Add)
        horizontal_box3.addWidget(button_Del)
        horizontal_box3.addWidget(button_Find)

        vertical_box = QVBoxLayout()
        vertical_box.addWidget(self.txtResult)
        vertical_box.addLayout(horizontal_box3)

        self.setLayout(vertical_box)
        self.show()

    def showGame(self, hp = 3, event = "test_case"):
        # 출력하고자하는 문자열 이 있는 부분입니다.
        hpText = "현재 가지고 있는 식량은 " + str(hp) +"개입니다."
        resultText = event + "사용자에게 이벤트를 보여주는 라인입니다."

        # UI에 출력을 하는 부분입니다.
        self.txtResult.setText("")

        for count in range(hp):
            self.txtResult.append(hpText)
            self.txtResult.append(resultText)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Game()
    sys.exit(app.exec_())