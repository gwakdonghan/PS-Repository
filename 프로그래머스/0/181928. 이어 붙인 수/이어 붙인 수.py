def solution(num_list):
    odd_str = ""  # 홀수를 이어 붙일 문자열
    even_str = ""  # 짝수를 이어 붙일 문자열
    
    for num in num_list:
        if num % 2 == 0:  # 짝수인지 확인
            even_str += str(num)  # 짝수이면 even_str에 추가
        else:  # 홀수인 경우
            odd_str += str(num)  # 홀수이면 odd_str에 추가
            
    odd_num = int(odd_str)  # 홀수 문자열을 정수로 변환
    even_num = int(even_str)  # 짝수 문자열을 정수로 변환
    
    return odd_num + even_num  # 두 수의 합 반환