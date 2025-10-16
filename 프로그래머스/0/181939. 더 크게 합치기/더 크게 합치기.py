def solution(a, b):
    ab = int(str(a) + str(b))  # a ⊕ b
    ba = int(str(b) + str(a))  # b ⊕ a
    return max(ab, ba)  # 더 큰 숫자 반환
