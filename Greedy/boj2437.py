#문제: 저울
#n개의 저울추로 만들 수 없는 양의 정수 무게중 최소값 구하기
#해결방법: 일단 다 더한값 + 1은 못만든다
#그럼 다 더한값에서 하나씩 줄여서 만들기?
#아직 못품... 1~x까지 현재 만들 수 있을 때, y 무게추가 있다면 y + x 까지 또 만들 수 있음 (질문글봄)
#근데 그러면 걍 무한정 만들수 있는거 아냐? ;; 얘의 조건이 뭐지.... 아 x와 y사이의 간극이 있으면 안되네  x + 1 = y 아니면 최소한 x=y여야하네
#그럼 조건이 현재 만들 수 있는 정수의 최대값 x < y 이면 그때부터는 못만드는구나! x...y 이 사이의 ...을 만들 수 없으니깐
#이런생각을 어떻게 하지... 대단하다. 많이 풀어서 닮아가는 수밖에 없구나라는 생각
def solve():
    n = int(input())
    weight = list(map(int, input().split(" ")))
    weight.sort()
    answer = 1
    for y in weight:
        if answer < y:
            break
        else:
            answer += y
        
    return answer

print(solve())