#문제: 별찍기 19
#해결방법: 일단 크게 생각한다. 짜피 다 찍어야하니깐
#일단 풀고 나서 한 생각: 재귀로 풀 수 있을 것 같다. 왜냐하면 패턴 반복이니깐
#내가 접근한 방식도 결국 " *" 추가에 집중해 그 사이의 값을 넣은거니깐... 
#확실히 재귀를 잘 못하는 것 같다. 기록해두고 연습할 것

def solve():
    n = int(input())
    length = 1 + 4 * (n-1)
    ans = []
    
    for i in range(length // 2 + 1): 
        
        if i % 2 == 0: 
            j = i // 2
            middle_row = (length - j * 2 * 2) * "*"
            row = '* ' * j + middle_row +' *' * j
        else:
            j = i // 2 + 1
            middle_row = (length - j * 2 * 2) * " "
            row = '* ' * j + middle_row +' *' * j
        
        ans.append(row)
    
    for i in range(length):
        if i < (length // 2 + 1):
            print(ans[i])
        else:
            print(ans[length - i - 1])
        
    
solve()