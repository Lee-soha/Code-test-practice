def solution(name, yearning, photo):
    answer = []
    dic = {}
    
    for k, v in zip(name, yearning):
        dic[k] = v
    
    for i in photo:
        num = 0
        for y in i:
            if y in name:
                num += dic[y]
        answer.append(num)
    
    return answer