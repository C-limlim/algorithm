#문제: 숫자카드게임
#가장 높은 숫자 카드 찾기
# n(행) x m(열), 행 선택 -> 가장 낮은 카드 선택

#해결방법
#각 행의 가장 작은 elment중 가장 큰 놈을 가진 행을 선택한다.

n, m = map(int, input().split(" "))
num = []
min_elm = []
for i in range(n):
    row = list(map(int, input().split(" ")))
    min_elm.append(min(row))

print(max(min_elm))
    


