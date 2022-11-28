

class Guess:

    def __init__(self, word):

        # 비밀로 선택된 단어
        self.secretWord = word
        # 추측한 단어를 담을 리스트
        self.guessedChars = []
        self.guessedStatus = " ".join(map(str, self.guessedChars))
        # 초기 아무것도 모르는 문자열의 의미로 다음을 출력합니다.
        self.blank_word = ["_" for _ in range(len(self.secretWord))]
        self.currentStatus = "".join(map(str, self.blank_word))

    def displayCurrent(self):
        return self.currentStatus

    def displayGuessed(self):
        return self.guessedStatus

    # 출력값이 boolean 타입이다.
    def guess(self, character):

        # 현재 문자가 self.guessedChars에 없기 때문에 추가한다.
        self.guessedChars.append(character)
        self.guessedStatus = " ".join(map(str, self.guessedChars))

        # 문자가 비밀 문자안에 들어 있지 않다면
        if character not in self.secretWord:
            # self.numTries 의 값을 1 증가 시킨다.
            return False
        # 문자다 비밀 문자열안에 들어 있다면
        else:
            # for 문을 통해 비밀문자의 각 단어에 접근한다.
            for count in range(len(self.secretWord)):
                # 만약 추측한 단어가 비밀 단어안에 있다면
                if self.secretWord[count] == character:
                    # self.blank_word 에 그 단어를 변경한다.
                    self.blank_word[count] = character
            self.currentStatus = "".join(map(str, self.blank_word))
            self.finished()

    def finished(self):

        if self.currentStatus == self.secretWord:
            return True
        else:
            return False