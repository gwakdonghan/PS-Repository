def solution(array):
    array.sort()  # 배열을 오름차순으로 정렬
    mid_index = len(array) // 2  # 중간 인덱스 찾기
    return array[mid_index]  # 중앙값 반환