
class Guess:

    def __init__(self, word):

        # 비밀로 선택된 단어
        self.secretWord = word
        # 현재 플레이어가 시도한 횟수로 초기값은 0이다.
        self.numTries = 0
        # 추측한 단어를 님을 리스트
        self.guessedChars = []
        # 초기 아무것도 모르는 문자열의 의미로 다음을 출력합니다.
        self.blank_word = ["_" for _ in range(len(self.secretWord))]
        self.currentStatus = "".join(map(str, self.blank_word))

    # 현재 까지의 추축을 출력하는 함수
    def display(self):
        print("Current: ", self.currentStatus)
        print("Tries: ", self.numTries)

    # 출력값이 boolean 타입이다.
    def guess(self, character):

        # 현재 문자가 self.guessedChars에 없기 때문에 추가한다.
        self.guessedChars.append(character)

        # 문자가 비밀 문자안에 들어 있지 않다면
        if character not in self.secretWord:
            # self.numTries 의 값을 1 증가 시킨다.
            self.numTries += 1
        # 문자다 비밀 문자열안에 들어 있다면
        else:
            # for 문을 통해 비밀문자의 각 단어에 접근한다.
            for count in range(len(self.secretWord)):
                # 만약 추측한 단어가 비밀 단어안에 있다면
                if self.secretWord[count] == character:
                    # self.blank_word 에 그 단어를 변경한다.
                    self.blank_word[count] = character
            self.currentStatus = "".join(map(str, self.blank_word))

            if self.currentStatus == self.secretWord:
                return True
            else:
                return False
