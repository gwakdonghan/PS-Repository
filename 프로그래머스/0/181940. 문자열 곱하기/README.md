<img width="1536" height="1208" alt="image" src="https://github.com/user-attachments/assets/780fd4a9-6b14-45ae-b4a0-db116b221768" />  

어떤 단어(문자열)를 몇 번 반복해서 길게 만든 다음,  
그걸 그대로 돌려주는 함수를 만드는 문제예요!  

예시:  
my_string = "string"  
k = 3  
- 단어 "string"을  
- 3번 반복하면 → "stringstringstring"  
👉 이걸 결과로 돌려주면 끝이에요!

🧠 그럼 어떻게 풀까?  
파이썬에서는 문자열도 곱셈이 가능해요!  

"abc" * 3  ➜ "abcabcabc"  

정답 코드:  
```
def solution(my_string, k):
    return my_string * k
```




