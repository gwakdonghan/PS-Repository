def solution(strlist):
    # 각 문자열의 길이를 계산하여 새로운 리스트로 반환
    lengths = [len(word) for word in strlist]
    return lengths