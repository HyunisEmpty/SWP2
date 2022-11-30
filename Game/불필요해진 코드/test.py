import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication, QLabel,
    QComboBox, QTextEdit, QLineEdit)
from PyQt5.QtCore import Qt

class ScoreDB(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        # self.dbfilename = 'assignment6.dat'
        # self.scoredb = []
        # self.readScoreDB()
        self.showScoreDB()

    def initUI(self):
        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Game')

        # QTextEdit (class 내 다른 함수에서 사용해야 해서 self. 를 추가함) 결과 화면
        self.txtResult = QTextEdit()

        # QLabel (각 라벨 이름정의)
        label_Name = QLabel('Name: ', self)
        label_Age = QLabel('Age: ', self)
        label_Score = QLabel('Score: ', self)
        label_Amount = QLabel('Amount: ', self)
        label_Key = QLabel('Key: ', self)
        label_Result = QLabel('Result: ', self)

        # QLineEdits 통해 입력을 받는 부분
        line_Name = QLineEdit("", self)
        line_Age = QLineEdit("", self)
        line_Score = QLineEdit("", self)
        line_Amount = QLineEdit("", self)

        # QComboBox 통해 Key 값을 정의한다.
        combo_Key = QComboBox()
        # 콤보박스에 Name, Age, Score 원소를 추가한다.
        key_list = ["Name", "Age", "Score"]
        combo_Key.addItems(key_list)

        # QPushButtons 통해 각 버튼을 정의하며 라벨에 맞는 버튼명으로 변수명을 정의한다.
        button_Add = QPushButton("Add", self)
        button_Del = QPushButton("Del", self)
        button_Find = QPushButton("Find", self)
        button_Inc = QPushButton("Inc", self)
        button_Show = QPushButton("Show", self)

        # 각 버튼이 눌리는 경우에 대하여 정의 한다.
        # Add 명령어는 Name, Age, Score 값을 인자값으로 넘겨줘야 한다.
        button_Add.clicked.connect(lambda: self.doScoreDb(self.scoredb, "Add " + line_Name.text() + " " + line_Age.text() + " " + line_Score.text()))
        # Del 은 원하는 이름을 지우는 것이 목적이기에 인자값으로 명령어와 이름만을 넘겨준다.
        button_Del.clicked.connect(lambda: self.doScoreDb(self.scoredb, "Del " + line_Name.text()))
        # Find 는 이름만을 보여주는 것이 목적이기에 인자값으로 명령어와 이름만을 넘겨준다.
        button_Find.clicked.connect(lambda: self.doScoreDb(self.scoredb, "Find " + line_Name.text()))
        # Inc 는 이름에 값을 더하는 것이 목적이기에 인자값으로 명령어와 이름과 값을 넘겨줍니다.
        button_Inc.clicked.connect(lambda: self.doScoreDb(self.scoredb, "Inc " + line_Name.text() + " " + line_Amount.text()))
        # show 는 currentText() 의 가장 최근값을 문자열 형태로 받아오는 것을 의미한다.
        button_Show.clicked.connect(lambda: self.doScoreDb(self.scoredb, "Show " + combo_Key.currentText()))

        # 첫번 QHBoxLayout
        horizontal_box1 = QHBoxLayout()

        horizontal_box1.addWidget(label_Name)
        horizontal_box1.addWidget(line_Name)
        horizontal_box1.addWidget(label_Age)
        horizontal_box1.addWidget(line_Age)
        horizontal_box1.addWidget(label_Score)
        horizontal_box1.addWidget(line_Score)

        # 두번 QHBoxLayout
        horizontal_box2 = QHBoxLayout()

        horizontal_box2.addStretch(1)                   # 수직방향 레이아웃 매니저의 addStretch 매소드로 여뱍을 제공
        horizontal_box2.addWidget(label_Amount)
        horizontal_box2.addWidget(line_Amount)
        horizontal_box2.addWidget(label_Key)
        horizontal_box2.addWidget(combo_Key)

        # 새번째 QHBoxLayout, 각 버튼들이 있는 줄이다.
        horizontal_box3 = QHBoxLayout()

        # horizontal_box3.addStretch(0)
        horizontal_box3.addWidget(button_Add)
        horizontal_box3.addWidget(button_Del)
        horizontal_box3.addWidget(button_Find)
        horizontal_box3.addWidget(button_Inc)
        horizontal_box3.addWidget(button_Show)

        # QVBoxLayout
        vertical_box = QVBoxLayout()

        vertical_box.addLayout(horizontal_box1)
        vertical_box.addLayout(horizontal_box2)
        vertical_box.addLayout(horizontal_box3)
        vertical_box.addWidget(label_Result)
        vertical_box.addWidget(self.txtResult)

        # setLayout 통해서 윈도우의 메인 레이아웃으로 설정한다.
        self.setLayout(vertical_box)
        self.show()

    # def closeEvent(self, event):
    #     self.writeScoreDB()

    # def readScoreDB(self):
    #     try:
    #         fH = open(self.dbfilename, 'rb')
    #     except FileNotFoundError as e:
    #         self.scoredb = []
    #         return
    #
    #     try:
    #         # 변수 = pickle.load(file)
    #         # 한줄씩 파일을 읽어오고 더이상 로드할 데이터가 없으면 EOFError 발생
    #         self.scoredb = pickle.load(fH)
    #     except:
    #         pass
    #     else:
    #         pass
    #     fH.close()

    # write the data into person db
    # def writeScoreDB(self):
    #     fH = open(self.dbfilename, 'wb')
    #     pickle.dump(self.scoredb, fH)
    #     fH.close()

    # 기본 키 값이 Name으로 정의되어 있고 인자값을 받을시에는 그값을 이용한다. (Default Parameter Value)
    def showScoreDB(self):
        resultText = ''
        # for p in sorted(self.scoredb, key=lambda person: person[keyname]):
        #     for attr in sorted(p):
        #         resultText += (attr + "=" + str(p[attr]) + "    ")
        #     resultText += "\n"
        self.txtResult.setText(resultText)

    # connect 호출시 항상 호출되는 함수로서 명령어는 저장하고 있는다.
    # def doScoreDb(self, scoredb, inputstr):
    #     parse = inputstr.split(" ")
    #
    #     # scoredb에 데이터를 저장하는 역활을 한다. Name과 Age그리고 Score를 입력받는다.
    #     if parse[0] == 'Add':
    #         record = {'Name': parse[1], 'Age': int(parse[2]), 'Score': int(parse[3])}
    #         scoredb += [record]
    #         self.showScoreDB()
    #
    #     # scoredb에 데이터를 지우는 역활을 합니다.
    #     elif parse[0] == 'Del':
    #         # scoredb[:]를 통해 복사한 리스트에서 값을 가져와 제거 함으르 누락되는 데이터가 없도록 한다.
    #         for p in scoredb[:]:
    #             if p['Name'] == parse[1]:
    #                 scoredb.remove(p)
    #         self.showScoreDB()
    #
    #     # comKey.currentText() : 현재 ComboBox에서 선택된 항목의 글자를 parse[1]에 반환 받는다.
    #     elif parse[0] == 'Show':
    #         sortKey = parse[1]
    #         self.showScoreDB(sortKey)
    #
    #     # parse 의 1에는 이름이 2에는 증가시키고자 하는 값이 들어가게 됩니다.
    #     elif parse[0] == 'Inc':
    #         for p in scoredb:
    #             if p['Name'] == parse[1]:
    #                 p['Score'] = int(p['Score']) + int(parse[2])
    #         self.showScoreDB()
    #
    #     # parse[1]에 입력된 이름이 맞다면 resultText에 저장하여 출력한다.
    #     elif parse[0] == 'Find':
    #         resultText = ''
    #         for p in scoredb:
    #             if p['Name'] == parse[1]:
    #                 for attr in sorted(p):
    #                     resultText += (attr + "=" + str(p[attr]) + "    ")
    #                 resultText += "\n"
    #         self.txtResult.setText(resultText)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())