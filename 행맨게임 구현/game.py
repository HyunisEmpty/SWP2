from hangman import Hangman     # hangman 의 Hangman 클래스 참조
from guess import Guess         # guess 의 Guess 클래스 참조
from word import Word           # word 의 Word 클래스 참조


def gameMain():
    # Word 클래스의 word 객체 생성
    word = Word('words.txt')
    # Guess 클래스의 guess 객체 생성
    guess = Guess(word.randFromDB())

    # 게임을 끝낼지 판단하는 boolean 형 finished define
    finished = False
    # Hangman 클래스의 hangman 객체 생성
    hangman = Hangman()
    # getLife 함수를 호출하여 시도 가능 횟수를 받아온다.
    maxTries = hangman.getLife()

    while guess.numTries < maxTries:
        hangman_display = hangman.get(maxTries - guess.numTries)
        print(hangman_display)
        guess.display()

        guessedChar = input('Select a letter: ')

        # 한단어가 아닌 이외의 값이 입력된 경우
        if len(guessedChar) != 1:
            print('One character at a time!')
            # 반복문을 처음부터 다시 시작
            continue

        # 이미 추축한 단어일때
        if guessedChar in guess.guessedChars:
            print('You already guessed \"' + guessedChar + '\"')
            # 반복문을 처음부터 다시 시작
            continue

        # 올바른 단어가 입력된 경
        finished = guess.guess(guessedChar)
        if finished:
            break

    # 성공한 경우
    if finished:
        print('Success')
    # 실패한 경우
    else:
        # 완성된 행맨 텍스트를 hangman 인스턴스를 통해 받아옴
        print(hangman.get(0))
        # 정답이 되는 문자열을 출력합니다.
        print('word [' + guess.secretWord + ']')
        # 현재까지 추축한 문자열을 출력합니다.
        print('guess [' + guess.currentStatus + ']')
        # Fail 출력
        print('Fail')

if __name__ == '__main__':
    gameMain()