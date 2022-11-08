numPadList = [
    '7', '8', '9',
    '4', '5', '6',
    '1', '2', '3',
    '0', '.', '=',
]

operatorList = [
    '*', '/',
    '+', '-',
    '(', ')',
    'C',
]

constantMap = [
    ('pi', '3.141592'),
    ('빛의 이동 속도 (m/s)', '3E+8'),
    ('소리의 이동 속도 (m/s)','340'),
    ('태양과의 평균 거리 (km)','1.5E+8'),
]
constantList = [x[0] for x in constantMap]

functionMap = [
    ('factorial (!)', 'factorial'),
    ('-> binary', 'decToBin'),
    ('binary -> dec', 'binToDec'),
    ('-> roman', 'decToRoman'),
    ('roman -> dec', 'romanToDec'),
]
functionList = [x[0] for x in functionMap]

romans = [
    (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
    (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
    (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
    (1, 'I')
]
