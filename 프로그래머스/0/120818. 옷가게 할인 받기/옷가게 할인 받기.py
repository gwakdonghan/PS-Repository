def solution(price):
    # 할인율 적용
    if price >= 500000:
        final_price = price * 0.8  # 20% 할인
    elif price >= 300000:
        final_price = price * 0.9  # 10% 할인
    elif price >= 100000:
        final_price = price * 0.95  # 5% 할인
    else:
        final_price = price  # 할인 없음

    # 소수점 이하 버리고 정수 반환
    return int(final_price)

# 테스트 케이스 실행
test_prices = [150000, 580000]
results = [solution(price) for price in test_prices]
results
