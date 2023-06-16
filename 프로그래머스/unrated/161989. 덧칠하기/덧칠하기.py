
def solution(n, m, section):
    answer = 1
    mi = min(section)
    for i in section:
        if i - mi >= m:
            answer += 1
            mi = i

    return answer
