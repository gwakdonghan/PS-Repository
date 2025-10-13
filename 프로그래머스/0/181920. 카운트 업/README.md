<img width="1720" height="890" alt="image" src="https://github.com/user-attachments/assets/b3264732-578a-4eea-aa5d-1ca5a9893e56" />  
🎯 문제 설명:  
어떤 숫자 start_num부터 end_num까지  
하나씩 차례대로 숫자를 세서 리스트에 담아주는 함수를 만들어야 해요.  

🧸 예를 들어 볼게요!  
만약 start_num = 3, end_num = 10 이라면?  
👉 3부터 10까지 차례대로 세면  
3, 4, 5, 6, 7, 8, 9, 10  
이 숫자들을 리스트로 담아야 해요.  
그래서 결과는: [3, 4, 5, 6, 7, 8, 9, 10]  

✅ 조건은 아주 쉬워요!  
숫자는 0부터 50 사이만 나와요.  
항상 start_num이 end_num보다 작거나 같아요.  
(그러니까 뒤로 숫자가 줄어들 일은 없어요!)  

🧠 정답 코드!  
```
def solution(start_num, end_num):
    answer = list(range(start_num, end_num + 1))
    return answer
```

🔍 정답 코드 설명!  
`def solution(start_num, end_num):`  
start_num부터 end_num까지 숫자를 받는 함수를 만들어요.  
`    answer = list(range(start_num, end_num + 1))`  
range(start_num, end_num + 1)  
👉 이건 start_num부터 end_num까지 숫자를 만들어주는 도구예요!  
+1을 꼭 해줘야 end_num도 포함돼요. (파이썬은 끝 숫자를 포함하지 않아요!)  
예: range(3, 11) → [3, 4, 5, 6, 7, 8, 9, 10]  
list(...)  
👉 숫자들을 리스트(목록) 로 바꿔줘요.  
예: list(range(3, 11)) → [3, 4, 5, 6, 7, 8, 9, 10]  
`    return answer`  
만든 리스트를 결과로 돌려줘요!  

예를 들어서:  
`solution(3, 10)`  
결과는:  
[3, 4, 5, 6, 7, 8, 9, 10]  


