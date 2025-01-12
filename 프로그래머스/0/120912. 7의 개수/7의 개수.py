def solution(array):
    count = 0
    for num in array:
        count += str(num).count('7')  # 숫자를 문자열로 바꾼 후 '7'의 개수를 셈
    return count

# 테스트
print(solution([7, 77, 17]))  # 출력: 4
print(solution([10, 29]))    # 출력: 0
