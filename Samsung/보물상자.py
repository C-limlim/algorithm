def solve():
    n, k = map(int, input().split(" "))
    number = list(input()) # list
    candidate_list = []
    number_in_line = n // 4
    for i in range(number_in_line):
        # 만들어진걸 append, 있으면 안넣는다
        number = number[1:] + [number[0]]
        a = "".join(number[:number_in_line])
        b = "".join(number[number_in_line: number_in_line * 2])
        c = "".join(number[number_in_line * 2: number_in_line * 3][::1])
        d = "".join(number[number_in_line * 3:][::1])
        
        for j in [a, b, c, d]:
            if j not in candidate_list:
                candidate_list.append(j)
     
             
    candidate_list.sort(reverse=True) 
    #print(candidate_list)  
    print(int(candidate_list[k - 1], 16))
        

t = int(input())
for _ in range(t):
    solve()