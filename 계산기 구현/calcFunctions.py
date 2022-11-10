from math import factorial as fact
from keypad import romans


# 팩토리얼 함수 구현
def factorial(numStr):
    try:
        n = int(numStr)
        r = str(fact(n))
    except:
        r = 'Error!'
    return r


# 10진수를 2진수로 변화하는 함수 구현
def decToBin(numStr):
    try:
        n = int(numStr)
        # bin 함수는 입력받은 integer 값을 2진수로 변환하여 출력한다.
        # oct(), hex() 가 있다.
        r = format(n, "b")
    except:
        r = 'Error!'
    return r


# 2진수를 10진수로 변환하는 함수 구현
def binToDec(numStr):
    try:
        # int("다른 진수", 2)는 다른 진수의 값을 2진수로 바꾸는 것이다. 여기에 인자 값으로 2, 8, 16이 온다
        n = int("0b" + str(numStr), 2)
        r = str(n)
    except:
        r = 'Error!'
    return r


# 10진수를 로마표기법으로 변경하는 함수 구현
def decToRoman(numStr):

    try:
        n = int(numStr)
    except:
        return 'Error!'

    if n >= 4000:
        return 'Error!'

    # 리스트의 경우
    r = ''
    for value, letters in romans:
        while n >= value:
            r += letters
            n -= value

    # 사전의 경우
    # r = ''
    # for value in sorted(romans.key(), reverse=True):
    #     while n >= value:
    #         r += romans[value]
    #         n -= value
    #
    return r

    """
    리스트의 경우 이미 정렬되어 있는 값을 가져오기에 추후에 정렬을 할 필요는 없습니다.
    사전의 경우 이미 정렬되어 있지 않기에 정렬을 하는 과정에서 불필요한 연산을 하게 됩니다.
    """

# 로마표기법을 10진수로 변경하는 함수 구현
def romanToDec(numStr):
    try:
        r = 0
        while len(numStr) != 0:
            for value, letters in romans:
                if numStr.find(letters) == 0:
                    r += value
                    if len(letters) == 2:
                        numStr = numStr[2:]
                    else:
                        numStr = numStr[1:]
    except:
        return 'Error!'

    return r