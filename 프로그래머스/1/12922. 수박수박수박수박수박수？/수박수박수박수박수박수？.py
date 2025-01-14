def solution(n):
    return ("수박" * (n // 2) + "수" * (n % 2))

# 테스트 예시
print(solution(3))  # "수박수"
print(solution(4))  # "수박수박"
