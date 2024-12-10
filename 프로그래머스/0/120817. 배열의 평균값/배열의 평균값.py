def solution(numbers):
    # 배열의 평균값 계산
    average = sum(numbers) / len(numbers)
    # 평균값을 .0 또는 .5로 반올림
    rounded_average = round(average * 2) / 2
    return rounded_average