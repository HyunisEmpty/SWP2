

class Hangman:
    text = [

        '''\
           ____
          |    |
          |    o
          |   /|\\
          |    |
          |   / \\
         _|_
        |   |______
        |          |
        |__________|\
        ''',

        '''\
           ____
          |    |
          |    o
          |   /|\\
          |    |
          |   /
         _|_
        |   |______
        |          |
        |__________|\
        ''',

        '''\
           ____
          |    |
          |    o
          |   /|\\
          |    |
          |
         _|_
        |   |______
        |          |
        |__________|\
        ''',

        '''\
           ____
          |    |
          |    o
          |   /|
          |    |
          |
         _|_
        |   |______
        |          |
        |__________|\
        ''',

        '''\
           ____
          |    |
          |    o
          |    |
          |    |
          |
         _|_
        |   |______
        |          |
        |__________|\
        ''',

        '''\
           ____
          |    |
          |    o
          |
          |
          |
         _|_
        |   |______
        |          |
        |__________|\
        ''',

        '''\
           ____
          |    |
          |
          |
          |
          |
         _|_
        |   |______
        |          |
        |__________|\
        ''',

    ]

    # 생성자
    def __init__(self):
        self.remainingLives = len(self.text) - 1;

    # self.remainingLives 값을 1 감소시키는 함수
    def decreaseLife(self):
        self.remainingLives -= 1

    def currentShape(self):
        return self.text[self.remainingLives]