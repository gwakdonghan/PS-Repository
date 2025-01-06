def solution(my_string, num1, num2):
    # 문자열을 리스트로 변환하여 문자 교환
    str_list = list(my_string)
    # 인덱스 num1과 num2의 문자 교환
    str_list[num1], str_list[num2] = str_list[num2], str_list[num1]
    # 다시 문자열로 변환하여 반환
    return ''.join(str_list)

# 테스트
print(solution("hello", 1, 2))  # "hlelo"
print(solution("I love you", 3, 6))  # "I lveo you"
