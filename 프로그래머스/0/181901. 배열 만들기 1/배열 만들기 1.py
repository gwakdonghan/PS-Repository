def solution(n, k):
    # 결과를 저장할 빈 리스트 생성
    result = []
    
    # 1부터 n까지 반복
    for i in range(1, n + 1):
        # i가 k의 배수인지 확인
        if i % k == 0:
            # k의 배수라면 리스트에 추가
            result.append(i)
    
    # 결과 리스트 반환
    return result
