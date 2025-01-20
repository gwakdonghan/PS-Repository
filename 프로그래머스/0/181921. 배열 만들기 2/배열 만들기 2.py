def solution(l, r):
    result = []
    for num in range(l, r+1):
        if all(c in '05' for c in str(num)):
            result.append(num)
    return result if result else [-1]

# 테스트 케이스
print(solution(5, 555))  # 출력: [5, 50, 55, 500, 505, 550, 555]
print(solution(10, 20))  # 출력: [-1]
