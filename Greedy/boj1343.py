#문제: 폴리오미노 | 2초, 128MB
#보드판이 .와 X로 구성될 때 (<=50)
#AAAA와 BB 로 겹침없이 X를 덮음, .는 덮으면 안됨
#사전순으로 가장 앞서는 답 출력. 덮을 수 없을경우 -1

#해결방법:
#4와 2의 조합... 홀수면 안됨...
#바로떠오르는 것: 연속 x의 개수가 홀수면 리턴한다. 그리고 4와 2의 배수로 채운다.
#근데 이방법 별로 안멋진듯... 풀래야 풀겠지만...

#더 좋은 풀이 발견
#input을 xxxx를 aaaa로, xx를 bb로 치환한다.
#그리고 x가 남아있다면 -1 리턴

def solve2():
    board = input()
    board = board.replace('XXXX', 'AAAA')
    board = board.replace('XX', 'AA')
    if 'X' in board:
        return -1
    else:
        return board
 

def solve():
    board = input().split(".")
    for i, piece in enumerate(board):
        if len(piece) == 0:
            pass
        
        if len(piece) % 2:
            return -1
        
        #4로 채울수 있으면 넣는다.
        count_a = len(piece) // 4
        count_b = (len(piece) - count_a * 4) // 2
        
        board[i] = 'AAAA'*count_a + 'BB'*count_b
    
    #바꿔서 보내기
    return ".".join(board)
    
print(solve())