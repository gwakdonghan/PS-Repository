def solution(array, n):
    count = 0  # 카운트를 0으로 초기화
    for num in array:  # 배열의 각 원소를 순회
        if num == n:  # 원소가 n과 같다면
            count += 1  # 카운트를 증가
    return count  # 최종 카운트를 반환