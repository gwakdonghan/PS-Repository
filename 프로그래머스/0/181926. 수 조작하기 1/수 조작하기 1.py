def solution(n, control):
    # control 문자열의 각 문자에 따라 n을 변경
    for command in control:
        if command == 'w':
            n += 1
        elif command == 's':
            n -= 1
        elif command == 'd':
            n += 10
        elif command == 'a':
            n -= 10
    return n