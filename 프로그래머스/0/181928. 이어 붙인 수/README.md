<img width="1488" height="1222" alt="image" src="https://github.com/user-attachments/assets/ee73daca-df43-45fc-be9c-2a4f1c4517aa" />  

리스트 num_list 안에 숫자가 있어요.  
이 숫자들을 홀수끼리 이어 붙인 수, 짝수끼리 이어 붙인 수를 만든 뒤  
두 수를 더해서 결과로 돌려주세요!  

정답 코드:  
```
def solution(num_list):
    odd = ''
    even = ''
    
    for num in num_list:
        if num % 2 == 0:  # 짝수면
            even += str(num)
        else:  # 홀수면
            odd += str(num)
    
    return int(odd) + int(even)
```
코드설명:  
odd = ''  
even = ''  
- 홀수랑 짝수를 문자처럼 붙이기 위해 빈 문자열 준비!

for num in num_list:  
- 리스트에서 하나씩 숫자를 꺼내요.  
  
    if num % 2 == 0:  
        even += str(num)  
- 짝수면 → 문자열로 바꿔서 even에 붙이기  
  
    else:  
        odd += str(num)
- 홀수면 → 문자열로 바꿔서 odd에 붙이기

return int(odd) + int(even)  
- 두 문자열을 숫자로 바꾼 뒤 더해서 리턴!


