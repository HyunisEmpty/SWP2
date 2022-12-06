from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLayout, QGridLayout
from PyQt5.QtWidgets import QTextEdit, QLineEdit, QToolButton

from hangman import Hangman     # hangman 의 Hangman 클래스 참조
from guess import Guess         # guess 의 Guess 클래스 참조
from word import Word           # word 의 Word 클래스 참조


class HangmanGame(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        # Word 클래스의 word 객체 생성
        self.word = Word("words.txt")

        # 행맨 상태 표시 위젯
        self.hangmanWindow = QTextEdit()               # QTextEdit 위젯을 이용
        self.hangmanWindow.setReadOnly(True)           # 읽기 전용
        self.hangmanWindow.setAlignment(Qt.AlignLeft)  # 왼쪽 정렬
        font = self.hangmanWindow.font()
        font.setFamily("Courier New")
        self.hangmanWindow.setFont(font)

        # 행맨 레이아웃
        hangmanLayout = QGridLayout()
        hangmanLayout.addWidget(self.hangmanWindow, 0, 0)

        # 게임 상태 표시 위젯들
        """
        currentWord-QLineEdit: readonly, center align
        guessedChars-QLineEdit: readonly
        message-QLineEdit: readonly
        guessButton-QToolButton-callbak : guessClicked
        charlnpuy-QLineEdit-maximum length:1
        newGameButton-QToolButton-callback: startGame()
        """

        # 현재 상태 레이아웃 생성
        statusLayout = QGridLayout()

        # 현재 단어 상태 표시 창
        self.currentWord = QLineEdit()
        self.currentWord.setReadOnly(True)                  # 읽기 전용 - 사용자에 의한 편집 불가
        self.currentWord.setAlignment(Qt.AlignCenter)       # 가운데 정렬
        font = self.currentWord.font()
        font.setPointSize(font.pointSize() + 8)             # 글꼴 크기 설정 (+8)
        self.currentWord.setFont(font)
        statusLayout.addWidget(self.currentWord, 0, 0, 1, 2)

        # 이미 사용된 글자들을 표시하기 위한 창
        self.guessedChars = QLineEdit()
        self.guessedChars.setReadOnly(True)
        self.guessedChars.setAlignment(Qt.AlignLeft)
        self.guessedChars.setMaxLength(52)
        statusLayout.addWidget(self.guessedChars, 1, 0, 1, 2)

        # 메시지 출력을 위한 창
        self.message = QLineEdit()
        self.message.setReadOnly(True)
        self.message.setAlignment(Qt.AlignLeft)
        self.message.setMaxLength(52)
        statusLayout.addWidget(self.message, 2, 0, 1, 2)

        # 사용자가 사용한 단어를 입력하는 줄
        self.charInput = QLineEdit()
        self.charInput.setMaxLength(1)
        statusLayout.addWidget(self.charInput, 3, 0)

        # 추측한 문자를 입력하기 위한 버튼
        self.guessButton = QToolButton()
        self.guessButton.setText('Guess!')
        # HnagmanGame.buttonClicked()를 구현하여 버튼이 눌리는 경우의 처리를 프로그래밍
        self.guessButton.clicked.connect(self.guessClicked)
        statusLayout.addWidget(self.guessButton, 3, 1)

        # 새로운 게임을 위한 버튼
        self.newGameButton = QToolButton()
        self.newGameButton.setText('New Game')
        self.newGameButton.clicked.connect(self.startGame)
        statusLayout.addWidget(self.newGameButton, 4, 0)

        # 위에서 구성한 두개의 레이아웃을 가로로 나란히 배치
        mainLayout = QGridLayout()
        mainLayout.addLayout(hangmanLayout, 0, 0)
        mainLayout.addLayout(statusLayout, 0, 1)

        # HangmanGame의 레이아웃을 mainLayout으로 지정
        self.setLayout(mainLayout)
        self.setWindowTitle("HangmanGame")

    def startGame(self):
        # Hangman 클래스의 hangman 객체 생성
        self.hangman = Hangman()
        # Guess 클래스의 guess 객체 생성, word instance의 randFromDB를 통해 무작위 단어를 받아
        self.guess = Guess(self.word.randFromDB())
        self.gameOver = False

        # hangmanWindow의 text를 행맨의 현재 상태로 초기화.
        self.hangmanWindow.setPlaceholderText(self.hangman.currentShape())
        # currentWord QLineEdit setText 통해서 정의 instance of guess 의 function displayCurrent
        self.currentWord.setText(self.guess.displayCurrent())
        # guessedChars QLineEdit setText 통해서 정의 instance of guess 의 function displayGuessed
        self.guessedChars.setText(self.guess.displayGuessed())
        # 메시지 출력창 초기화
        self.message.clear()

    def guessClicked(self):
        guessedChar = self.charInput.text()
        # 문자 입력창 초기화
        self.charInput.clear()
        # 메시지 출력칭 초기화
        self.message.clear()

        # 만약 gameOver가 True라면 게임 끝
        if self.gameOver == True:
            # 메시지 출력하고 - message.setText() - 리턴
            return self.message.setText("Game Over")

        # 입력의 길이가 1 인지를 판단하고, 아닌 경우 메시지 출력, 리턴
        if len(guessedChar) != 1:
            return self.message.setText("One character at a time!")

        # 이미 사용한 글자인지를 판단하고, 아닌 경우 메시지 출력, 리턴
        if guessedChar in self.guess.guessedChars:
            return self.message.setText('You already guessed \"' + guessedChar + '\"')

        success = self.guess.guess(guessedChar)
        if success == False:
            # 남아 있는 목숨을 1 만큼 감소
            self.hangman.decreaseLife()
            # 메시지 출력
            self.message.setText("secert word 안에 없는 문자!")

        # hangmanWindow 에 현재 hangman 상태 그림을 출력
        self.hangmanWindow.setPlaceholderText(self.hangman.currentShape())
        # currentWord 에 현재까지 부분적으로 맞추어진 단어 상태를 출력
        self.currentWord.setText(self.guess.displayCurrent())
        # guessedChars 에 지금까지 이용한 글자들의 집합을 출력
        self.guessedChars.setText(self.guess.displayGuessed())

        if self.guess.finished():
            # 메시지 ("Success!") 출력하고, self.gameOver 는 True 로
            self.message.setText("Success!")
            self.gameOver = True

        elif self.hangman.getRemainingLives() == 0:
            # 메시지 ("Fail!" + 비밀 단어) 출력하고, self.gameOver 는 True 로
            self.message.setText("Fail! " + self.guess.secretWord)
            self.gameOver = True


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    game = HangmanGame()
    game.show()
    sys.exit(app.exec_())