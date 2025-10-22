<img width="1468" height="778" alt="image" src="https://github.com/user-attachments/assets/bd15d3f8-d9fc-4a89-a6cf-be5da7e10b79" />  

문자 리스트를 하나의 문자열로 바꾸는 문제  

리스트 arr 안에 글자(문자)들이 있어요.  
이 글자들을 차례대로 붙여서 하나의 문자열로 만들고 그 문자열을 return(반환) 하면 돼요!  

예시:  
arr = ["a", "b", "c"]  
- 이걸 "abc"로 이어붙이면 돼요!

출력:  
"abc"  

어떻게 붙일까?  
파이썬에서는 문자열 리스트를 .join() 이라는 걸로 쉽게 붙일 수 있어요!  
"".join(["a", "b", "c"])  ➜  "abc"  

정답 코드:  
```
def solution(arr):
    return ''.join(arr)
```

코드 설명:  
`''.join(arr)` arr 리스트 안의 문자들을 전부 이어붙임  

예시 테스트:  
solution(["a", "b", "c"])  ➜  "abc"  
solution(["h", "e", "l", "l", "o"])  ➜  "hello"  






