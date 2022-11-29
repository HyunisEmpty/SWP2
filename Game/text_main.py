import random

game_event = ["누군가 방공호의 문을 두드립니다. 문을 여시겠습니까?",
              "당신이 방심한 사이 쥐가 나타나서 당신의 식량을 먹었습니다...",
              "한노인 찾아와 식량을 1만큼만 달라고 합니다. 주시겠습니까?",
              "누군가 방공호의 문을 두드립니다. 문을 여시겠습니까?",
              "방공호 근처에 있는 사슴을 사냥하려고 합니다. 미끼를 사용하시겠습니까?",
              "방공호 근처에 있는 사슴을 사냥하려고 합니다. 미끼를 사용하시겠습니까?"]
game_event_input = ["yes 혹은 no를 입력해주세요",
                    "아무키나 입력해주세요",
                    "yes 혹은 no를 입력해주세요",
                    "yes 혹은 no를 입력해주세요",
                    "yes 혹은 no를 입력해주세요",
                    "yes 혹은 no를 입력해주세요",]
game_event_yes_food = [2, -1, -1, -2, 3, -1]
game_event_yes = ["그는 자원보상자로 당신에게 식략을 전달해줍니다. 식량 +" + str(game_event_yes_food[0]),
                  "쥐가 2만큼의 식량을 먹었습니다. 식량 " + str(game_event_yes_food[1]),
                  "노인은 급하게 밥을 먹어치우고 사라집니다. 식량 " + str(game_event_yes_food[2]),
                  "그는 무장강도로 당신의 식량을 뺐어 갑니다. 식량 " + str(game_event_yes_food[3]),
                  "당신은 사냥에 성공했습니다. 식량 +" + str(game_event_yes_food[4]),
                  "당신은 사냥에 실패했습니다. 식량 +" + str(game_event_yes_food[5])]
game_event_no_food = [0, -2, 0, -1, 0, 0]
game_event_no = ["한참 문을 두드리다. 문앞의 사람은 떠납니다.",
                 "쥐가 2만큼의 식량을 먹었습니다. 식량 -2",
                 "식량을 주지 않으니 노인은 화를내며 사라집니다.",
                 "그는 당장 문을열지 않으면 죽이겠다고 소리쳤지만, 곧 문앞에서 사라졌습니다. 식량 -1",
                 "사슴 사냥에 실패 했습니다.",
                 "사슴 사냥에 실패 했습니다."]
game_item = ["구급약", "책"]
game_item_text = ", ".join(map(str, game_item))


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
            # 게임을 시작
            if Answer(answer) == True:
                day += 1
            else:
                break
        else:
            for count in range(2):
                event_number = random.randrange(0, len(game_event) )
                print("")
                print("남은 식량 :" + str(food) + "개 ,오늘은 " + str(day) + "일차입니다.")
                print("현재 가지고 있는 아이템 : " + game_item_text )
                print(game_event[event_number])
                print(game_event_input[event_number])
                answer = input("입력해주세요 :")
                # 게임을 시작
                if(game_event_input[event_number] == "yes 혹은 no를 입력해주세요"):
                    if Answer(answer) == True:
                        print( "게임 메시지 :" + game_event_yes[event_number])
                        food += game_event_yes_food[event_number]
                    elif Answer(answer) == False:
                        print(game_event_no[event_number])
                        food += game_event_no_food[event_number]
                    else:
                        print("잘못된 입력입니다.")
                else:
                    print(game_event_no[event_number])
                    food += game_event_no_food[event_number]
            day += 1

            print("")
            print(str(day) + "일차가 마무리됩니다.")
            print("굶주린 당신은 식량을 하나 먹습니다.")
            food -= 1
            print("남은 식량 :" + str(food) + "개 ,오늘은 " + str(day) + "일차입니다.")
            answer = input("아무키나 입력해주세요 :")
            DayEnd(answer)


    if food == 0:
        print("식량이 떨어져서 당신은 굶어 죽었습니다...")


def Answer(answer):
    if answer == "yes":
        return True
    elif answer == "no":
        return False
    else:
        return "input error"

def DayEnd(answer):
    print("")


# 게임을 시작
Game()