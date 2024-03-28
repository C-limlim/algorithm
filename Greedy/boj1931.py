#회의실 배정: 2초, 128MB
#회의 I개에 대해 회의실을 겹치지 않게 쓸 수 있게 하는 최대 회의 수
#회의의 시작하는 시간과 끝나는 시간이 같을 수 있음, +1하면 됨
#풀이: 먼저 끝나는것을 채워준다.
#틀린점: 시작과 끝이 같을 수 있으므로, 단순하게 끝시작으로만 소팅하면 안된다.

def solve():
    n = int(input())
    meeting = []
    for _ in range(n):
        meeting.append(tuple(map(int, input().split(" "))))     
    meeting = sorted(meeting, key=lambda x: (x[-1], x[0])) 
    
    count = 1
    curr = 0
    
    for next in range(1, n):
        if meeting[curr][1] > meeting[next][0]:
            continue
        #현재 미팅 끝나는 시각이 다음 미팅 시작 시간보다 작거나 같을 때
        curr = next
        count += 1

    print(count)

solve()