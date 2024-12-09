def solution(n):
    return sum(i for i in range(2, n + 1, 2))

# 테스트 예시
print(solution(10))  # 결과: 30
print(solution(4))   # 결과: 6