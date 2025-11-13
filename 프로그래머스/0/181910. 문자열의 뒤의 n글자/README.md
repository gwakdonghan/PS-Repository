<img width="1598" height="1150" alt="image" src="https://github.com/user-attachments/assets/70065ea9-cd19-4ae5-ae2f-ec484715709c" />  

문제 설명:  

문자열 my_string과 숫자 n이 주어져요.
이 문자열의 뒤에서부터 n글자만 뽑아서
그것만 돌려주는 함수(solution)를 만들면 된다.  

예시:  
```
my_string = "He110W0r1d"
n = 5
```
결과: "W0r1d"  

정답 코드:  
```
def solution(my_string, n):
    return my_string[-n:]
```

코드 설명:  
my_string[-n:]  
👉 문자열에서 뒤에서부터 n글자만 잘라오는 파이썬 문법이다.  

예:  
```
"hello"[-2:]  ➜  "lo"
"abcdef"[-3:] ➜  "def"
```
  
파이썬 슬라이싱([])은 자주 쓰이니까 익숙해지면 좋다.

