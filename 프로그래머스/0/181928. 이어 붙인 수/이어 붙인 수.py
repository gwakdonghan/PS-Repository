def solution(num_list):
    odd = ''
    even = ''
    
    for num in num_list:
        if num % 2 == 0:  # 짝수면
            even += str(num)
        else:  # 홀수면
            odd += str(num)
    
    return int(odd) + int(even)
