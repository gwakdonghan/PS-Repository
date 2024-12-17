def solution(sides):
    longest = max(sides)  # 가장 긴 변
    other_sum = sum(sides) - longest  # 나머지 두 변의 합
    
    if longest < other_sum:
        return 1  # 삼각형을 만들 수 있음
    else:
        return 2  # 삼각형을 만들 수 없음