#문제: 알바생 강호 | 2초, 256 MB
#팁 최대값 구하기
#팁: 원래생각한팁 - (커피받은등수 -1), 음수이면 0
#1등부터 시작

#해결방법
#돈 많이 내는 사람이 먼저 와라
#이게 왜 될까? -> 가장 높은 tip 받는걸 반복하다보면 최대합을 가진다.

def solve():
    n = int(input())
    tips = []
    for i in range(n):
        tips.append(int(input()))
    
    tips.sort(reverse=True)
    order = 1
    ans = 0
    for tip in tips:
        money = tip - order + 1
        if money > 0:
            order += 1
            ans += money
    return ans
    
print(solve())