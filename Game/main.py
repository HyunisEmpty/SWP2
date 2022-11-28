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

    def showGame(self):
        resultText = "사용자에게 게임 시스템을 출력할 부분 입니다."
        self.txtResult.setText(resultText)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Game()
    sys.exit(app.exec_())