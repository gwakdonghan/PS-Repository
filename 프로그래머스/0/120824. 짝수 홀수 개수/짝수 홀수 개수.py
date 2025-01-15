def solution(num_list):
    # 짝수 개수와 홀수 개수 계산
    even_count = sum(1 for num in num_list if num % 2 == 0)  # 짝수는 2로 나누어 떨어짐
    odd_count = len(num_list) - even_count  # 전체 길이에서 짝수 개수 빼면 홀수 개수
    return [even_count, odd_count]
