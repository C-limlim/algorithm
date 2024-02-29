#문제: 상하좌우
#(1,1) to (n,n)의 정사각형
# LRUD로 한칸 이동, 정사각형 공간 벗어나는 움직임은 무시

#해결: 다 해본다. log(N)

def solve():
    n = int(input())
    LRUD = input().split(" ")
    
    point = [1, 1]
    
    for direction in LRUD:
        if direction == "L" and point[1] > 1:
            point[1] -= 1
        elif direction == "R" and point[1] < n:
            point[1] += 1
        elif direction == "U" and point[0] > 1:
            point[0] -= 1
        elif direction == "D" and point[0] < n:
            point[0] += 1
        else:
            pass
    
    print(point[0], point[1])
    
solve()