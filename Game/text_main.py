from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtWidgets import QLayout, QGridLayout
from PyQt5.QtWidgets import QTextEdit, QLineEdit, QToolButton

import random
from text_event import (game_event, game_event_input, game_event_yes_food,
                        game_event_yes, game_event_no_food, game_event_no,
                        first_text, game_item, game_item_event_1, game_item_event_1_input,
                        game_item_event_1_no, game_item_event_1_yes, game_item_event_2_input,
                        game_item_event_2_yes_food, game_item_event_2_yes, game_item_event_2_no_food,
                        game_item_event_2_no, end_message)

game_item_text = ", ".join(map(str, game_item))

class SurvivorGame(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.item_counter = 0
        self.InputCounter = 0
        self.food = -1
        self.day = -1
        # 플레이어의 진행에 따라 달라지는 식량과 두번의 이벤트 마다 증가하는 날짜를 출력
        self.food_day_string = "남은 식량 :" + str(self.food) + "개 ,오늘은 " + str(self.day) + "일차입니다."

        # 메시지 출력을 위한 창
        self.message = QLineEdit()
        self.message.setReadOnly(True)
        self.message.setAlignment(Qt.AlignLeft)

        # 아이템 출력을 위한 창
        self.item_window = QLineEdit()
        self.item_window.setReadOnly(True)
        self.item_window.setAlignment(Qt.AlignLeft)

        # 게임 중요 텍스트 출력 위젯
        self.textWindow = QTextEdit()               # QTextEdit 위젯을 이용
        self.textWindow.setReadOnly(True)           # 읽기 전용
        self.textWindow.setAlignment(Qt.AlignLeft)  # 왼쪽 정렬
        font = self.textWindow.font()
        font.setFamily("Courier New")               # 폰트 관련 정의
        self.textWindow.setFont(font)

        # text, 텍스트 레이아웃
        textLayout = QGridLayout()
        textLayout.addWidget(self.message, 0, 0)
        textLayout.addWidget(self.item_window, 1, 0)
        textLayout.addWidget(self.textWindow, 2, 0)

        # status, 현재 상태 레이아웃 생성
        statusLayout = QGridLayout()

        # status, 사용자의 대답을 입력하는 창
        self.stringInput = QLineEdit()
        statusLayout.addWidget(self.stringInput, 1, 0)

        # status, 사용자의 대답을 입력하는 버튼
        self.InputButton = QToolButton()
        self.InputButton.setText('입력!')
        self.InputButton.clicked.connect(self.InputClicked)
        statusLayout.addWidget(self.InputButton, 1, 1)

        # status, 게임의 진행을 위해 눌러야 하는 버튼
        self.nextButton = QToolButton()
        self.nextButton.setText('다음')
        self.nextButton.clicked.connect(self.NextClicked)
        statusLayout.addWidget(self.nextButton, 1, 2)

        # status, 새로운 게임을 위한 버튼
        self.newGameButton = QToolButton()
        self.newGameButton.setText('새로운 게임')
        self.newGameButton.clicked.connect(self.startGame)
        statusLayout.addWidget(self.newGameButton, 2, 0)

        # main, 위에서 구성한 두개의 레이아웃을 가로로 나란히 배치
        mainLayout = QGridLayout()
        mainLayout.addLayout(textLayout, 0, 0)
        mainLayout.addLayout(statusLayout, 1, 0)

        self.setLayout(mainLayout)                       # SurvivorGame의 레이아웃을 mainLayout으로 지정
        self.setWindowTitle("SurvivorGame")              # SurvivorGame의 Title 정의

    def startGame(self):
        gameOver = False
        self.food = 10
        self.day = 1
        # 게임룰을 설명하는 초기 설정
        self.message.setText(self.food_day_string)
        self.item_window.setText("현재 가지고 있는 아이템 :" + game_item_text)
        self.textWindow.append(first_text)

    # 다음 버튼이 눌린경우 호출된는 함수
    def NextClicked(self):
        if self.food <= 0:
            self.textWindow.append(end_message)
        else:
            # 랜덤한 이벤트를 받아온다
            self.event_number = random.randrange(0, len(game_event))
            self.message.setText(self.food_day_string)
            self.textWindow.append("")
            self.textWindow.append(game_event[self.event_number])
            self.textWindow.append(game_event_input[self.event_number])

    # 잘못된 입력이 있을 경우 이전과 동일한 이벤트를 출력하는 함수
    def RecallNextClicked(self):
        self.message.setText(self.food_day_string)
        self.textWindow.append("")
        self.textWindow.append(game_event[self.event_number])
        self.textWindow.append(game_event_input[self.event_number])

    def InputClicked(self):
        # 식량이 0이하인지 확인한다. 0이하인 경우 게임을 끝낸다.
        if self.food <= 0:
            self.textWindow.append(end_message)
        else:
            self.answer = self.stringInput.text()       # 입력창에 있는 문자를 받아옴.
            self.textWindow.append("")

            if (game_event_input[self.event_number] == "yes 혹은 no를 입력해주세요 :"):                                         # 입력에 대한 경우가 yes or no인 경우
                if self.answer == "yes":                                                                                    # yes인 경우
                    self.textWindow.append("게임 메시지 :" + game_event_yes[self.event_number])
                    self.food += game_event_yes_food[self.event_number]
                    self.message.setText(self.food_day_string)
                    self.InputCounter += 1
                elif self.answer == "no":                                                                                   # no인 경우
                    self.textWindow.append("게임 메시지 :" + game_event_no[self.event_number])
                    self.food += game_event_no_food[self.event_number]
                    self.message.setText(self.food_day_string)
                    self.InputCounter += 1
                # 입력이 잘못된 경우 self.RecallNextClicked()를 다시 호출하여 동일한 이벤트를 출력함
                else:
                    self.textWindow.append("게임 메시지 :잘못된 입력입니다. 동일한 이벤트를 다시 호출합니다.")
                    self.RecallNextClicked()

            self.stringInput.setText("")

            if self.InputCounter == 2:
                self.DayChangeMessage()

    def DayChangeMessage(self):
        self.textWindow.append("")
        self.textWindow.append(str(self.day) + "일차가 마무리됩니다.")
        self.textWindow.append("굶주린 당신은 식량을 하나 먹습니다. 식량 -1")
        self.day += 1
        self.food -= 1
        self.message.setText("남은 식량 :" + str(self.food) + "개 ,오늘은 " + str(self.day) + "일차입니다.")
        self.InputCounter = 0



if __name__ == '__main__':
    import sys
    food = 10
    day = 1
    gameOver = False
    app = QApplication(sys.argv)
    game = SurvivorGame()
    game.show()
    sys.exit(app.exec_())

# 게임의 주요 메소드가 구현되는 함수 Game
# def Game():
#     # food = 10
#     # day = 0
#     # 게임이 처음 시작되었을때 사용자에게 보여주는 텍스트입니다.
#     print("""공습경보가 울렸고 당신은 방공호로 대피했습니다.
# 당신은 앞으로 이 방공호 안에서 생존해야합니다.
# 여러 사건이 발생하며 최대한 오래 생존하세요.
# 하루에 식량 하나를 소비하며, 식량이 0이되면 게임은 종료 됩니다.
# 게임을 시작하려면 yes를 입력해주세요""")
#
#     while food > 0:
#
#         # 첫날의 경우
#         if day == 0:
#             answer = input("입력해주세요 :")
#             print("")
#             # 게임을 시작
#             if Answer(answer) == True:
#                 day += 1
#             else:
#                 break
#         else:
#             # 하루에 2개의 이벤트가 발생합니다.
#             for count in range(2):
#                 # random을 이용해 이벤트중 무작위 이벤트를 받아온다
#                 event_number = random.randrange(0, len(game_event) )
#
#                 print("남은 식량 :" + str(food) + "개 ,오늘은 " + str(day) + "일차입니다.")
#                 # print("현재 가지고 있는 아이템 : " + game_item_text )
#                 print(game_event[event_number])
#                 # print(game_event_input[event_number])
#                 answer = input(game_event_input[event_number])
#                 print("")
#
#
#                 # 게임을 시작
#                 if(game_event_input[event_number] == "yes 혹은 no를 입력해주세요 :"):
#                     if Answer(answer) == True:
#                         print( "게임 메시지 :" + game_event_yes[event_number])
#                         food += game_event_yes_food[event_number]
#                     elif Answer(answer) == False:
#                         print("게임 메시지 :" + game_event_no[event_number])
#                         food += game_event_no_food[event_number]
#                     else:
#                         print("잘못된 입력입니다.")
#                     answer = input("확인하셨다면 아무키나 눌러주세요 :")
#                 else:
#                     print(game_event_no[event_number])
#                     food += game_event_no_food[event_number]
#                     answer = input("확인하셨다면 아무키나 눌러주세요 :")
#                 print("")
#
#             # 2번의 이벤트가 day 1증가 food 1감소합니다.
#             day += 1
#             food -= 1
#             DayEndDisplay(food, day)
#             answer = input("아무키나 입력해주세요 :")
#             print("")
#
#
#     if food <= 0:
#         print("식량이 떨어져서 당신은 굶어 죽었습니다...")


# def DayEndDisplay(food, day):
#     print(str(day) + "일차가 마무리됩니다.")
#     print("굶주린 당신은 식량을 하나 먹습니다. 식량 -1")
#     print("남은 식량 :" + str(food) + "개 ,오늘은 " + str(day) + "일차입니다.")


# 게임을 시작
# Game()