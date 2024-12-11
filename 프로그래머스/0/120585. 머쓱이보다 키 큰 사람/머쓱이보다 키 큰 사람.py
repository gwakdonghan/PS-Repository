def solution(array, height):
    # 머쓱이보다 큰 사람의 수를 저장할 변수
    count = 0
    
    # 배열을 순회하며 머쓱이의 키와 비교
    for friend_height in array:
        if friend_height > height:
            count += 1  # 머쓱이보다 크면 count를 증가
    
    return count