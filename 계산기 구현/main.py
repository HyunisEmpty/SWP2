from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLineEdit, QToolButton
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QLayout, QGridLayout

from keypad import numPadList, operatorList, constantList, functionList, constantMap, functionMap
import calcFunctions

class Button(QToolButton):

    def __init__(self, text, callback):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setText(text)
        self.clicked.connect(callback)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 20)
        size.setWidth(max(size.width(), size.height()))
        return size


class Calculator(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        # Display Window
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setMaxLength(15)

        # 레이아웃을 정의한다.
        numLayout = QGridLayout()
        opLayout = QGridLayout()
        constLayout = QGridLayout()
        funcLayout = QGridLayout()

        buttonGroups = {
            'num': {'buttons': numPadList, 'layout': numLayout, 'columns': 3},
            'op': {'buttons': operatorList, 'layout': opLayout, 'columns': 2},
            'constants': {'buttons': constantList, 'layout': constLayout, 'columns': 1},
            'functions': {'buttons': functionList, 'layout': funcLayout, 'columns': 1},
        }
        # num, op, constants, functions 키들을 label 변수에 담는다.
        for label in buttonGroups.keys():
            r = 0; c = 0
            # 각 키값에 대응하는 값들을 buttonPad 변수에 가지고 온다.
            buttonPad = buttonGroups[label]
            # 각버튼 키에 해당하는 List 를 받아온다.
            for btnText in buttonPad['buttons']:
                button = Button(btnText, self.buttonClicked)
                # buttonPad 의 키 layout 을 통해서 현재의 변수값을 어디에 저장할지 정의 한다.
                buttonPad['layout'].addWidget(button, r, c)
                c += 1
                if c >= buttonPad['columns']:
                    c = 0; r += 1

        # Layout
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)

        # 각 레이아웃의 위치를 정의한다.
        mainLayout.addWidget(self.display, 0, 0, 1, 2)
        mainLayout.addLayout(numLayout, 1, 0)
        mainLayout.addLayout(opLayout, 1, 1)
        mainLayout.addLayout(constLayout, 2, 0)
        mainLayout.addLayout(funcLayout, 2, 1)

        self.setLayout(mainLayout)

        self.setWindowTitle("My Calculator")


    def buttonClicked(self):

        # 만약 이전 연산으로 Error 를 출력했다면 새로운 버튼이 눌렸을때 창의 내용을 지운다.
        if self.display.text() == 'Error!':
            self.display.setText('')

        # 현재 눌린 버튼을 sender()함수를 통해서 받아온다.
        button = self.sender()
        # key 에 눌린 버튼의 텍스트를 받아온다.
        key = button.text()

        # 만약 입력받은 텍스트가 = 라면
        if key == '=':
            try:
                # 현재 텍스트값을 eval함수로 넘겨서 그 값을 result에 저장한다.
                result = str(eval(self.display.text()))
            except:
                result = 'Error!'
            self.display.setText(result)

        # 만약 입력받은 텍스가 = 라면
        elif key == 'C':
            # 현재 디스플레이 텍스트를 초기화 한다.
            self.display.clear()

        #  만약 key 값이 constantList 들어가 있다면 키 값에 해당하는 값을 불러온다.
        elif key in constantList:
            self.display.setText(self.display.text() + constantMap[constantList.index(key)])

        # 만약 key 값이 functionList 들어가 있다면 키 값에 해당하는 값을 불러온다.
        elif key in functionList:
            num = self.display.text()
            func = eval("calcFunctions." + functionMap[functionList.index(key)][1])
            self.display.setText(str(func(num)))

        else:
            self.display.setText(self.display.text() + key)


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())