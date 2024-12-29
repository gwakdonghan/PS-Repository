def solution(myString, pat):
    # 대소문자를 구분하지 않으므로 모든 문자열을 소문자로 변환
    myString = myString.lower()
    pat = pat.lower()
    
    # pat이 myString에 포함되어 있는지 확인
    if pat in myString:
        return 1  # 존재하면 1 반환
    else:
        return 0  # 존재하지 않으면 0 반환
