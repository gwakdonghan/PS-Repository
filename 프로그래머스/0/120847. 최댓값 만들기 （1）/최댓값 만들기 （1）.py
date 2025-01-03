def solution(numbers):
    # 배열을 내림차순으로 정렬
    numbers.sort(reverse=True)
    # 가장 큰 두 숫자의 곱 반환
    return numbers[0] * numbers[1]

# 테스트 케이스
print(solution([1, 2, 3, 4, 5]))  # 출력: 20
print(solution([0, 31, 24, 10, 1, 9]))  # 출력: 744
