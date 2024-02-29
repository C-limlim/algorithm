#문제: 왕실의 나이트
#8x8 보드판,  L자 (수평2칸수직1칸 / 수평1칸수직2칸)
#나이트의 위치에 따른 이동 경우의 수

#해결방법: 다 해보기

def solve2():
    #이렇게 일일히 하지말고 미리 값을 세팅해두기
    input_data = input()
    row = int(input_data[1])
    col = int(ord(input_data[0])-ord(input_data[1])) + 1
    steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
    result = 0
    for step in steps:
        next_row = row + step[0]
        next_col = col + step[1]
        
        if next_row > 0 and next_row < 9 and next_col > 0 and next_col <9:
            result += 1
    print(result)

def solve():
    point = list(input())
    point[0] = ord(point[0]) - 96 #ascii 'a' is 97
    point[1] = int(point[1])
    count = 0
    
    #case1. hor +2
    if point[0] + 2 < 9:
        if point[1] + 1 < 9:
            count += 1
        if point[1] - 1 > 0:
            count += 1
    
    if point[0] -2 > 0:
        if point[1] + 1 < 9:
            count += 1
        if point[1] - 1 > 0:
            count += 1
    
    if point[1] + 2 < 9:
        if point[0] + 1 < 9:
            count += 1
        if point[0] - 1 > 0:
            count += 1
    
    if point[1] - 2 > 0:
        if point[0] + 1 < 9:
            count += 1
        if point[0] - 1 > 0:
            count += 1
     
    print(count)
    
    
solve()