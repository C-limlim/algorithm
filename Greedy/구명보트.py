#문제: 구명보트
#최대 2명 탑승가능하고 무게제한이 있는 구명보트
#모든사람을 구출하기 위해 필요한 구명보트 개수의 최소값
#무인도 사람 1~50000, 몸무게 및 무게제한 범위 40kg~240kg
#무게제한은 항상 사람들의 몸무게중 최댓값보다 크게 주어지므로 구출할 수 없는 경우는 없음

#무거운 사람부터 보내버려... 그리고 걔의 짝이 있으면 같이 태워버려...

def solution(people, limit):
    #효율성 못통과한 이유: pop(0)을 하면 뒤의 데이터를 한칸씩 당겨 O(n)이 됨
    #people을 deque로 만들어 popleft를 사용하면 더 빠름
    
    people.sort()
    boat = 0
    partner_id = -1
    fat_person_id = len(people)
    saved = len(people)
    
    while len(people) > 0:
        person = people.pop(-1)
        
        #태울 수 있는 사람이 있는지 확인
        partner_id = -1
        for i, candidate in enumerate(people):
            if candidate + person <= limit:
                partner_id = i
            else: #이친구는 같이 탈 수 없습니다.
                break
        
        if partner_id != -1:
            people.pop(partner_id)
            
        boat += 1
        
    return boat

# 효율성 테스트를 위한 코드 변경
def solution2(people, limit):
    people.sort()
    boat = 0
    partner_id = 0
    fat_person_id = len(people) - 1
    
    while True: ## 이걸 left < right로 하는게 더 간결하군. 
        if fat_person_id < partner_id:
           break
        elif fat_person_id == partner_id:
           boat += 1
           break
       
        #생각해보면 제일 무거운친구한테 제일 가벼운 친구 매칭시켜주고 되면 보내면 되잔아?
        if people[fat_person_id] + people[partner_id] <= limit:
            partner_id += 1
        
        fat_person_id -= 1
        boat += 1
        
    return boat

print(solution2([70, 50, 80, 50], 100))