def solution(n):
    if n % 2 == 1:  # 홀수면
        return sum(i for i in range(1, n + 1, 2))  # 홀수만 더함
    else:  # 짝수면
        return sum(i ** 2 for i in range(2, n + 1, 2))  # 짝수 제곱 더함
