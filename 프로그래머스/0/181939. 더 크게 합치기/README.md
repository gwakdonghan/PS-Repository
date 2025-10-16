<img width="1564" height="1288" alt="image" src="https://github.com/user-attachments/assets/6f440d77-b0d7-485d-b155-236789a34e42" />  

숫자 두 개를 붙여서 만든 숫자들 중 더 큰 숫자를 골라서 돌려주기!  

🧩 어떻게 붙이냐고?  
예를 들어 숫자 a = 12, b = 3이 있다면, 두 가지 방법으로 붙일 수 있어요:  
1. a ⊕ b ➜ 12랑 3을 붙이니까 123  
2. b ⊕ a ➜ 3랑 12를 붙이니까 312  
그러면 그중에서 더 큰 숫자(312) 를 결과로 돌려줘야 해요!  

정답 코드:  
```
def solution(a, b):
    ab = int(str(a) + str(b))  # a ⊕ b
    ba = int(str(b) + str(a))  # b ⊕ a
    return max(ab, ba)  # 더 큰 숫자 반환
```

코드 설명:  
`ab = int(str(a) + str(b))`  
- 숫자 a와 b를 문자(str) 로 바꿔서 붙여요.
- 예: a=9, b=91이면 → '9' + '91' = '991'
- 다시 숫자로 바꿔서 ab = 991이 돼요.

`ba = int(str(b) + str(a))`  
- 이번엔 반대로 붙여요.
- 예: '91' + '9' = '919' → 숫자 919

`return max(ab, ba)`  
- 두 숫자 중에 더 큰 숫자를 고르고 돌려줘요!

