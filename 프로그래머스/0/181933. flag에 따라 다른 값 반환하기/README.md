<img width="1718" height="1250" alt="image" src="https://github.com/user-attachments/assets/8b8e2ba2-cab2-4b2d-ba6c-b5f2700b21ce" />
“flag 값에 따라 다른 계산을 하기”  
flag 뜻:  
프로그래밍에서 자주 등장하는 **flag**는 단순히 "깃발"이 아니라, 특정 상태나 조건을 나타내는 표시 변수를 의미합니다.  


| 단어       | 한국어 의미                         | 프로그래밍 용도                   |
| -------- | ------------------------------ | -------------------------- |
| **flag** | **플래그**, **표시 변수**, **상태 표시기** | 어떤 조건이나 상태가 참/거짓인지 저장하는 변수 |  

🧠 쉽게 말하면?  
flag는 무언가의 상태를 기억해두기 위한 변수예요.  
주로 True / False 같은 불리언 값을 사용해요.  

```
found = False  # flag 변수 초기화

for num in [1, 2, 3, 4]:
    if num == 3:
        found = True  # 조건을 만족하면 flag 변경

if found:
    print("3이 리스트에 있어요!")
else:
    print("3이 없어요.")
```

- 여기서 found가 flag 변수예요.
- 특정 조건이 **만족되었는지(=상태 체크)**를 알려주는 역할을 하죠.

🎯 언제 사용하나요?  
- 반복문에서 특정 조건이 만족됐는지 추적할 때
- 어떤 작업을 한 번만 수행하게 만들 때
- 에러가 발생했는지 감지할 때
- 옵션 설정값을 나타낼 때

🧠 그러니까 flag는…  
- 처음엔 False (못 찾음)  
- 찾으면 True (찾았어!)  
이렇게 바뀌는 '표시판' 같은 역할을 해요!  

📘 요약하자면: 🔹 flag = 어떤 상태를 표시해주는 변수 (보통 True / False)
상황이나 조건을 추적하고 제어하는 데 매우 유용합니다.

---
🧠 문제를 쉽게 설명:  
- 숫자 a, b, 그리고 flag 라는 값이 있어요.
- 이때, flag가 True면 ➜ a + b를 해요.
- flag가 False면 ➜ a - b를 해요.
그리고 그 결과를 돌려주는 함수를 만들면 돼요.

🧸 예시로 볼게요  
```
a = -4  
b = 7  
flag = True
```  
- flag가 True니까 ➜ a + b = -4 + 7 = 3
- 결과는 → 3

```
a = -4  
b = 7  
flag = False
```
- flag가 False니까 ➜ a - b = -4 - 7 = -11
- 결과는 → -11

✅ 정답 코드 !
```
def solution(a, b, flag):
    if flag:  # flag가 True면
        return a + b
    else:     # flag가 False면
        return a - b
```
정답코드 설명:  
`def solution(a, b, flag):`
- 이건 a, b, flag라는 값을 받아서 계산하는 함수예요.
`    if flag:`
- 만약 flag가 True면...
`        return a + b`
두 숫자를 더해서 돌려줘요!
```
    else:
        return a - b
```
아니면(flag가 False면) ➜ 두 숫자를 빼서 돌려줘요!  

요약!  
| flag 값 | 계산 방식 | 예시 (a=-4, b=7) | 결과  |
| ------ | ----- | -------------- | --- |
| True   | a + b | -4 + 7         | 3   |
| False  | a - b | -4 - 7         | -11 |












