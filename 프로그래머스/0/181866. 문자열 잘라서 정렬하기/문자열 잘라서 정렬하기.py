def solution(myString):
    # "x"를 기준으로 문자열을 나눕니다.
    split_strings = myString.split("x")
    # 빈 문자열은 제외하고 사전순으로 정렬합니다.
    result = sorted([s for s in split_strings if s])
    return result

# 테스트 예시
print(solution("axbxcxdx"))  # ["a", "b", "c", "d"]
print(solution("dxccxbbbxaaaa"))  # ["aaaa", "bbb", "cc", "d"]
