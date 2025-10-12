<img width="2048" height="1097" alt="image" src="https://github.com/user-attachments/assets/161255c6-b8b0-48cb-b3bc-1bc40cefc961" />
📘 문제 설명 :

컴퓨터가 두 개의 단어를 공백(띄어쓰기) 으로 나눠서 입력으로 줘요.
예를 들어 apple pen 이런 식으로요.

우리는 그 두 단어를 그냥 이어붙여서 출력하면 돼요.  
→ 즉, applepen 이렇게!  
  
🎯 해야 하는 일
단어 두 개를 띄어쓰기 없이 붙여서 출력하기!  
  
📏 조건
단어 하나의 길이는 1글자 이상 10글자 이하예요.  
항상 딱 두 개의 단어만 입력돼요.  

---
정답 코드 :  
```
# 두 개의 단어를 입력받아서
str1, str2 = input().strip().split(' ')

# 그냥 이어 붙여서 출력하면 끝!
print(str1 + str2)
```

코드 풀이 :  
1. 첫 번째 줄  
`str1, str2 = input().strip().split(' ')`  
이 줄에서 하는 일:

input()  
👉 사용자가 키보드로 입력한 글자를 받아와요.  
예: apple pen 이라고 입력하면 이게 문자열로 들어와요.  
  
.strip()  
👉 혹시 입력할 때 앞뒤에 빈칸(공백) 이 있으면 없애줘요.  
예: ' apple pen ' → 'apple pen'  
  
.split(' ')  
👉 공백(띄어쓰기) 을 기준으로 나눠요.  
예: 'apple pen' → ['apple', 'pen'] (리스트로 나눔!)  
  
str1, str2 = ...  
👉 나눠진 두 단어를 각각 str1과 str2에 저장해요.  
예: str1 = 'apple', str2 = 'pen'  

2. 두 번째 줄  
`print(str1 + str2)`  
이 줄에서 하는 일:  

str1 + str2  
👉 두 단어를 붙여요!  
예: 'apple' + 'pen' → 'applepen'  
  
print(...)  
👉 결과를 화면에 출력해요!  

---
💬 마무리 정리  
입력받은 두 단어를  
나눠서(str1, str2)  
그냥 붙여서 출력하면 되는 아주 간단한 문제예요!


