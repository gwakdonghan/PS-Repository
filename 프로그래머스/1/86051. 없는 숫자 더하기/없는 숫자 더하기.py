def solution(numbers):
    # 0부터 9까지 모든 숫자의 합에서, numbers에 있는 숫자의 합을 뺀다.
    full_sum = sum(range(10))  # 0부터 9까지의 합: 0 + 1 + 2 + ... + 9 = 45
    numbers_sum = sum(numbers)  # numbers 배열의 숫자들의 합
    return full_sum - numbers_sum

# 테스트 케이스
print(solution([1, 2, 3, 4, 6, 7, 8, 0]))  # 출력: 14
print(solution([5, 8, 4, 0, 6, 7, 9]))     # 출력: 6
