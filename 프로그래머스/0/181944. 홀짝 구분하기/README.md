<img width="1366" height="1330" alt="image" src="https://github.com/user-attachments/assets/bb8b6164-3d67-4137-a673-0e183697abb2" />  

“홀짝 구분하기” 문제  

자연수 n이 입력으로 주어졌을 때,  
n이 짝수면 → "n is even"  
n이 홀수면 → "n is odd"  
라는 문장을 출력해주는 프로그램을 만들어요.  

조건  
- 입력값 n은 1부터 1000까지의 자연수입니다.
- 짝수는 2, 4, 6, 8처럼 2로 나누어 떨어지는 수예요.
- 홀수는 1, 3, 5, 7처럼 2로 나누어 떨어지지 않는 수예요.

정답 코드:  
```
a = int(input())  # 사용자로부터 숫자를 입력받아서 a에 저장

if a % 2 == 0:  # 2로 나누어 떨어지면 짝수
    print(f"{a} is even")
else:  # 아니면 홀수
    print(f"{a} is odd")
```
코드 설명:  
`a = int(input())` 숫자를 입력받고 정수로 바꿔서 저장해요.    
`if a % 2 == 0:` 2로 나눴을 때 나머지가 0이면 짝수예요.  
`print(f"{a} is even")` 짝수면 이렇게 출력.  
`else:` 짝수가 아니면 무조건 홀수!  
`print(f"{a} is odd")` 그래서 홀수면 이렇게 출력해요.  

