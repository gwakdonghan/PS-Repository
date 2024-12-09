def solution(angle):
    if 0 < angle < 90:
        return 1  # 예각
    elif angle == 90:
        return 2  # 직각
    elif 90 < angle < 180:
        return 3  # 둔각
    elif angle == 180:
        return 4  # 평각

# 테스트 예시
print(solution(70))   # 결과: 1
print(solution(91))   # 결과: 3
print(solution(180))  # 결과: 4