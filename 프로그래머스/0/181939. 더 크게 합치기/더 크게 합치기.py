def solution(a, b):
    # a ⊕ b 계산
    ab = int(str(a) + str(b))
    # b ⊕ a 계산
    ba = int(str(b) + str(a))
    # 더 큰 값을 반환
    return max(ab, ba)