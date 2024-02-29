#문제: 시각
#3이 포함된 시각의 모든 경우의 수 구하기

#해결방법: 모름.. 다센다?
#아니면 미리 계산? 쉽게가자..
#하루는 86400이니까 다 돌려도 됨.

def solve():
    n = int(input())
    count = 0
    for hour in range(n + 1):
        for minute in range(60):
            for second in range(60):
                time = str(hour)+str(minute)+str(second)
                if '3' in time:
                    count += 1
    
    print(count)
    
    
solve()