def solution(my_string, overwrite_string, s):
    # s부터 overwrite_string의 길이만큼 잘라내고 overwrite_string으로 교체
    return my_string[:s] + overwrite_string + my_string[s+len(overwrite_string):]

# 예시 실행
print(solution("He11oWorld", "lloWorl", 2))  # 출력: HelloWorld
print(solution("Program29b8UYP", "merS123", 7))  # 출력: ProgrammerS123