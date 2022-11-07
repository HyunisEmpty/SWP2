from math import factorial as fact
# from keypad import romans

def factorial(numStr):
    try:
        n = int(numStr)
        r = str(fact(n))
    except:
        r = 'Error!'
    return r

def decToBin(numStr):
    try:
        n = int(numStr)
        # bin 함수는 입력받은 integer 값을 2진수로 변환하여 출력한다.
        # oct(), hex() 가 있다.
        r = bin(n)[2:]
    except:
        r = 'Error!'
    return r

def binToDec(numStr):
    try:
        # int("다른 진수", 2)는 다른 진수의 값을 2진수로 바꾸는 것이다. 여기에 인자 값으로 2, 8, 16이 온다
        n = int(numStr, 2)
        r = str(n)
    except:
        r = 'Error!'
    return r

def decToRoman(numStr):
    try:
        n = int(numStr)
    except:
        return 'Error!'

    if n >= 4000:
        return 'Error!'

    r = ''
    for value, letters in romans:
        while n >= value:
            r += letters
            n -= value

    return r

def romanToDec(numStr):
    try:
        r = 0
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