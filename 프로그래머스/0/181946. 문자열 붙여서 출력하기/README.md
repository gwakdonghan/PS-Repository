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
~~~
# 두 개의 단어를 입력받아서
str1, str2 = input().strip().split(' ')

# 그냥 이어 붙여서 출력하면 끝!
print(str1 + str2)
~~~
코드 풀이 :  
~str1, str2 = input().strip().split(' ')~  

