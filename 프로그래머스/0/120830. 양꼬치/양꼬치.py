def solution(n, k):
    # 무료로 제공된 음료수의 개수
    free_drinks_given = n // 10
    
    # 유료로 계산해야 하는 음료수의 개수
    payable_drinks = k - free_drinks_given
    
    # 총 비용 계산
    total_cost = (n * 12000) + (payable_drinks * 2000)
    
    return total_cost