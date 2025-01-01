def solution(my_string):
    # 문자열을 공백 기준으로 분리하여 리스트로 반환
    return my_string.split()

# 예제 입력
print(solution("i love you"))  # 출력: ["i", "love", "you"]
print(solution("programmers"))  # 출력: ["programmers"]
