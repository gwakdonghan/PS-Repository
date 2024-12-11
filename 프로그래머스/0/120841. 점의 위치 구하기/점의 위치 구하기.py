def solution(dot):
    x, y = dot[0], dot[1]  # x, y 좌표 분리
    if x > 0 and y > 0:    # 1사분면
        return 1
    elif x < 0 and y > 0:  # 2사분면
        return 2
    elif x < 0 and y < 0:  # 3사분면
        return 3
    elif x > 0 and y < 0:  # 4사분면
        return 4