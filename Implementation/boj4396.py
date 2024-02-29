#문제: 지뢰찾기
#지뢰 위치 & 눌림/안눌린 버튼 확인해서 지뢰 몇개있는지 써주기
square = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 0], [0, 1], [1, -1], [1, 0], [1, 1]]

def solve():
    n = int(input())
    game_over = False
    answer = []
    play = []
    for _ in range(n):
        row = list(input())
        answer.append(row)
    for _ in range(n):
        row = list(input())
        play.append(row)
        
    for i, arr in enumerate(play):
        for j, elm in enumerate(arr):
            if elm == 'x':
                play[i][j] = count_star(n, i, j, answer)
                if play[i][j] == "*":
                    game_over = True
            
    for i in range(n):
        for j in range(n):
            if game_over and answer[i][j] == '*':
                print('*', end="")
            else:
                print(play[i][j], end="")
        print()     

def count_star(n, i, j, answer):
    count = 0
    if answer[i][j] == '*':
        return '*'
    
    for pos in square:
        new_i = i + pos[0]
        new_j = j + pos[1]
        if new_i < 0 or new_i > n - 1 or new_j < 0 or new_j > n - 1:
            continue
        
        if answer[new_i][new_j] == '*':
            count += 1
        
    return count

solve()