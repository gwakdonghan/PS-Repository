def solution(num_list):
    # 마지막 원소와 그 전 원소를 확인
    last = num_list[-1]
    second_last = num_list[-2]

    # 마지막 원소가 그 전 원소보다 클 경우
    if last > second_last:
        diff = last - second_last
        num_list.append(diff)
    else:
        double_last = last * 2
        num_list.append(double_last)

    return num_list
