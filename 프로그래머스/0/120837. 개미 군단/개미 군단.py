def solution(hp):
    # 각 개미의 공격력
    general_ant = 5
    soldier_ant = 3
    worker_ant = 1

    # 장군개미로 최대한 공격
    generals = hp // general_ant
    remaining_hp = hp % general_ant

    # 병정개미로 공격
    soldiers = remaining_hp // soldier_ant
    remaining_hp %= soldier_ant

    # 일개미로 남은 HP 처리
    workers = remaining_hp // worker_ant

    # 총 개미 수 반환
    return generals + soldiers + workers

# 테스트 케이스 실행
test_cases = [23, 24, 999]
results = [solution(hp) for hp in test_cases]
results
