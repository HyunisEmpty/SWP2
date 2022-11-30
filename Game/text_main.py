import random
from text_event import game_event, game_event_input, game_event_yes_food, game_event_yes, game_event_no_food, game_event_no

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtWidgets import QLayout, QGridLayout
from PyQt5.QtWidgets import QTextEdit, QLineEdit, QToolButton


# 아이템의 경우 아직 미구현 된 시스템
# game_item = ["구급약", "책"]
# game_item_text = ", ".join(map(str, game_item))

class SurvivorGame(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        # Word 클래스의 word 객체 생성
        # self.word = Word("words.txt")

        # self.label_Name = QLabel('게임 메시지', self)

        # 메시지 출력을 위한 창
        self.message = QLineEdit()
        self.message.setReadOnly(True)
        self.message.setAlignment(Qt.AlignLeft)
        self.message.setMaxLength(52)

        # 행맨 상태 표시 위젯
        self.hangmanWindow = QTextEdit()               # QTextEdit 위젯을 이용
        self.hangmanWindow.setReadOnly(True)           # 읽기 전용
        self.hangmanWindow.setAlignment(Qt.AlignLeft)  # 왼쪽 정렬
        font = self.hangmanWindow.font()
        font.setFamily("Courier New")
        self.hangmanWindow.setFont(font)

        # 행맨 레이아웃
        hangmanLayout = QGridLayout()
        # hangmanLayout.addWidget(self.label_Name, 0, 0)
        hangmanLayout.addWidget(self.message, 0, 0)
        hangmanLayout.addWidget(self.hangmanWindow, 1, 0)

        # 현재 상태 레이아웃 생성
        statusLayout = QGridLayout()

        # 현재 단어 상태 표시 창
        # self.currentWord = QLineEdit()
        # self.currentWord.setReadOnly(True)                  # 읽기 전용 - 사용자에 의한 편집 불가
        # self.currentWord.setAlignment(Qt.AlignCenter)       # 가운데 정렬
        # font = self.currentWord.font()
        # font.setPointSize(font.pointSize() + 8)             # 글꼴 크기 설정 (+8)
        # self.currentWord.setFont(font)
        # statusLayout.addWidget(self.currentWord, 0, 0, 1, 2)

        # 이미 사용된 글자들을 표시하기 위한 창
        # self.guessedChars = QLineEdit()
        # self.guessedChars.setReadOnly(True)
        # self.guessedChars.setAlignment(Qt.AlignLeft)
        # self.guessedChars.setMaxLength(52)
        # statusLayout.addWidget(self.guessedChars, 1, 0, 1, 2)

        # 사용자가 사용한 단어를 입력하는 줄
        self.charInput = QLineEdit()
        # self.charInput.setMaxLength(1)
        statusLayout.addWidget(self.charInput, 1, 0)

        # 추측한 문자를 입력하기 위한 버튼
        self.guessButton = QToolButton()
        self.guessButton.setText('입력!')
        # HnagmanGame.buttonClicked()를 구현하여 버튼이 눌리는 경우의 처리를 프로그래밍
        # self.guessButton.clicked.connect(self.guessClicked)
        statusLayout.addWidget(self.guessButton, 1, 1)

        # 새로운 게임을 위한 버튼
        self.newGameButton = QToolButton()
        self.newGameButton.setText('새로운 게임')
        self.newGameButton.clicked.connect(self.startGame)
        statusLayout.addWidget(self.newGameButton, 2, 0)

        # 위에서 구성한 두개의 레이아웃을 가로로 나란히 배치
        mainLayout = QGridLayout()
        mainLayout.addLayout(hangmanLayout, 0, 0)
        mainLayout.addLayout(statusLayout, 1, 0)

        # HangmanGame의 레이아웃을 mainLayout으로 지정
        self.setLayout(mainLayout)
        self.setWindowTitle("SurvivorGame")

    def startGame(self):
        # # Hangman 클래스의 hangman 객체 생성
        # self.hangman = Hangman()
        # # Guess 클래스의 guess 객체 생성, word instance의 randFromDB를 통해 무작위 단어를 받아
        # self.guess = Guess(self.word.randFromDB())
        self.gameOver = False

        # hangmanWindow의 text를 행맨의 현재 상태로 초기화.
        self.hangmanWindow.setPlaceholderText("""공습경보가 울렸고 당신은 방공호로 대피했습니다.
당신은 앞으로 이 방공호 안에서 생존해야합니다.
여러 사건이 발생하며 최대한 오래 생존하세요.
하루에 식량 하나를 소비하며, 식량이 0이되면 게임은 종료 됩니다.
게임을 시작하려면 yes를 입력해주세요""")
        # currentWord QLineEdit setText 통해서 정의 instance of guess 의 function displayCurrent
        # self.currentWord.setText(self.guess.displayCurrent())
        # guessedChars QLineEdit setText 통해서 정의 instance of guess 의 function displayGuessed
        # self.guessedChars.setText(self.guess.displayGuessed())
        # 메시지 출력창 초기화
        self.message.clear()

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    game = SurvivorGame()
    game.show()
    sys.exit(app.exec_())

# 게임의 주요 메소드가 구현되는 함수 Game
def Game():
    food = 10
    day = 0
    # 게임이 처음 시작되었을때 사용자에게 보여주는 텍스트입니다.
    print("""공습경보가 울렸고 당신은 방공호로 대피했습니다.
당신은 앞으로 이 방공호 안에서 생존해야합니다.
여러 사건이 발생하며 최대한 오래 생존하세요.
하루에 식량 하나를 소비하며, 식량이 0이되면 게임은 종료 됩니다.
게임을 시작하려면 yes를 입력해주세요""")

    while food > 0:

        # 첫날의 경우
        if day == 0:
            answer = input("입력해주세요 :")
            print("")
            # 게임을 시작
            if Answer(answer) == True:
                day += 1
            else:
                break
        else:
            # 하루에 2개의 이벤트가 발생합니다.
            for count in range(2):
                # random을 이용해 이벤트중 무작위 이벤트를 받아온다
                event_number = random.randrange(0, len(game_event) )
                
                print("남은 식량 :" + str(food) + "개 ,오늘은 " + str(day) + "일차입니다.")
                # print("현재 가지고 있는 아이템 : " + game_item_text )
                print(game_event[event_number])
                # print(game_event_input[event_number])
                answer = input(game_event_input[event_number])
                print("")


                # 게임을 시작
                if(game_event_input[event_number] == "yes 혹은 no를 입력해주세요 :"):
                    if Answer(answer) == True:
                        print( "게임 메시지 :" + game_event_yes[event_number])
                        food += game_event_yes_food[event_number]
                    elif Answer(answer) == False:
                        print("게임 메시지 :" + game_event_no[event_number])
                        food += game_event_no_food[event_number]
                    else:
                        print("잘못된 입력입니다.")
                    answer = input("확인하셨다면 아무키나 눌러주세요 :")
                else:
                    print(game_event_no[event_number])
                    food += game_event_no_food[event_number]
                    answer = input("확인하셨다면 아무키나 눌러주세요 :")
                print("")

            # 2번의 이벤트가 day 1증가 food 1감소합니다.
            day += 1
            food -= 1
            DayEndDisplay(food, day)
            answer = input("아무키나 입력해주세요 :")
            print("")


    if food <= 0:
        print("식량이 떨어져서 당신은 굶어 죽었습니다...")


def Answer(answer):
    if answer == "yes":
        return True
    elif answer == "no":
        return False
    else:
        return "input error"

def DayEndDisplay(food, day):
    print(str(day) + "일차가 마무리됩니다.")
    print("굶주린 당신은 식량을 하나 먹습니다. 식량 -1")
    print("남은 식량 :" + str(food) + "개 ,오늘은 " + str(day) + "일차입니다.")


# 게임을 시작
Game()