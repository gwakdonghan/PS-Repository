def solution(numbers):
    result = []  # 결과를 저장할 빈 리스트를 만듭니다
    for num in numbers:  # numbers 배열의 각 숫자(num)를 하나씩 가져옵니다
        result.append(num * 2)  # num에 2를 곱한 값을 결과(result)에 추가합니다
    return result  # 결과 리스트를 반환합니다

# 예제 테스트
print(solution([1, 2, 3, 4, 5]))  # 출력: [2, 4, 6, 8, 10]
print(solution([1, 2, 100, -99, 1, 2, 3]))  # 출력: [2, 4, 200, -198, 2, 4, 6]
