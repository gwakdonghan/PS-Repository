def solution(num, n):
    if num % n == 0:  # num이 n의 배수인지 확인
        return 1      # 배수라면 1 반환
    else:
        return 0      # 배수가 아니라면 0 반환