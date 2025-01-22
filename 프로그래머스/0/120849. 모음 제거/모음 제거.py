def solution(my_string):
    vowels = {'a', 'e', 'i', 'o', 'u'}  # 모음을 집합으로 정의
    # 문자열에서 모음을 제거
    result = ''.join(char for char in my_string if char not in vowels)
    return result

# 테스트
print(solution("bus"))  # 출력: "bs"
print(solution("nice to meet you"))  # 출력: "nc t mt y"
