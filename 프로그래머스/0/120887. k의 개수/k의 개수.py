def solution(i, j, k):
    # k를 문자열로 변환
    k = str(k)
    # i부터 j까지 숫자 생성 및 문자열 변환 후 k의 등장 횟수 세기
    count = sum(str(num).count(k) for num in range(i, j + 1))
    return count

# 예시 테스트
example_1 = solution(1, 13, 1)  # Expected: 6
example_2 = solution(10, 50, 5)  # Expected: 5
example_3 = solution(3, 10, 2)  # Expected: 0

example_1, example_2, example_3
