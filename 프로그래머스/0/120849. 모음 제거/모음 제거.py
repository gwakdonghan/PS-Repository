def solution(my_string):
    # 제거할 모음 리스트
    vowels = "aeiou"
    # 문자열을 순회하며 모음이 아닌 문자만 골라서 join
    result = ''.join(char for char in my_string if char not in vowels)
    return result

# 테스트
print(solution("bus"))  # 출력: "bs"
print(solution("nice to meet you"))  # 출력: "nc t mt y"
