def solution(cipher, code):
    # code 번째마다의 문자만 추출
    result = cipher[code-1::code]
    return result

# 테스트 코드
print(solution("dfjardstddetckdaccccdegk", 4))  # 출력: "attack"
print(solution("pfqallllabwaoclk", 2))         # 출력: "fallback"
