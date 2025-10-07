def solution(num_list, n):
    """
    num_list의 n 번째 원소(인덱스 n-1)부터
    마지막 원소까지를 잘라내어 반환합니다.
    """
    # n 번째 원소는 인덱스로 'n - 1'입니다.
    # [시작 인덱스:] 형태로 리스트 끝까지 슬라이싱합니다.
    return num_list[n-1:]