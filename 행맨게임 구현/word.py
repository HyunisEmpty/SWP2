import random

# 텍스트 파일로부터 텍스트를 읽어 임의의 문자를 선정하여 출력하는 class
class Word:

    # 초기화 생성자, 파일을 읽어들여서 단어 데이터 베이스 초기화
    def __init__(self, filename):

        # words 리스트 정의
        self.words = []
        # f에 filename 파일을 읽기 모드로 받아 옴
        f = open(filename, 'r')
        # lines 리스트에 파일을 한줄씩 받아옴
        lines = f.readlines()
        # 파일을 닫음
        f.close()

        # count 변수를 정의함
        self.count = 0
        # line에 lines리스트에 문자열을 하나씩 받아옴
        for line in lines:
            # word에 line 문자열의 개행문자를 제거하여 저장함
            word = line.rstrip()
            # words리스트에 word를 저장
            self.words.append(word)
            # count 변수의 값을 1 증가 시킴
            self.count += 1

    # 난수 생성 함수
    def randFromDB(self):

        # 단어 데이터베이스의 인덱스 범위 내에서 난수를 발생시켜서 해당 위치의 단어를 리턴
        r = random.randrange(self.count)
        return self.words[r]

