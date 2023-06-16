def solution(players, callings):
    answer = []
    dic = {} # 이름 : 등수
    dic2 = {} # 등수 : 이름
    for i, y in enumerate(players):
        dic[y] = i
        dic2[i] = y
    for call in callings:
        loc = dic[call]
        loc2 = loc -1
        name = dic2[loc2]
        dic[dic2[loc]] = loc2
        dic[dic2[loc2]] = loc
        dic2[loc] = name
        dic2[loc2] = call
    answer = sorted(dic, key=lambda x: dic[x])
    
        
    return answer