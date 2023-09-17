## 알고리즘이란?
- 문제 해결 방법을 정의한 '일련의 단계적 절차'이자 어떠한 문제를 해결하기 위한 '동작들의 모임'

## 알고리즘의 성능 지표
1. effectiveness(효과성) : 문제를 해결하였는가, 필요충분조건이다.
2. efficiency(효율성) : 리소스(메모리 등)를 작게 사용했는가

    ### Time complexity
    - Big-O notation으로 표현
    - 문제를 해결하는데 걸린 반복 횟수
    - 실행 시간이 아닌 이유는 기기 성능에 따라 달라지기 때문이다

    ### Space complexity
    - 프로그램이 사용하는 공간(리소스)의 복잡도
    - 코드 프로파일링시 확인

## Time complextiy vs Space complexcity
- Time complextiy를 더욱 중요하게 다룬다.
- Time complexiity가 복잡하다는 것은 우리가 원하는 시간 내에 완료하는 것이 불가능 하다는 것
- 메모리가 부족하다면 그냥 추가해서 해결할 수도 있다

## Big-O notation
- 가장 오래걸리는 상한을 표시한다.
- ex) 4n + n log n + 10 -> O(n log n)

## 재귀함수 vs 비재귀함수
- 재귀함수의 대표적인 예 : 피보나치 수열, 팩토리얼 계산
- 재귀함수와 비재귀함수 중 어느것이 더 빠르게 계산할까?
  - 일반적으로 비재귀함수가 더 빠르다.
- 재귀함수의 장점
  - 코드가 깔끔해진다. 

## Code example
```python
def On_simple_search(lst,number):  # O(n)
    is_found = False
    for num in lst:
        if num == number:
            is_found = True
            break
    return is_found
```

```python
def On2_bubble_sort(lst):  # O(n^2)
    for i in range(len(lst)-1):
        for j in range(len(lst)-1-i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
return lst
```
```python
i = n    # O(log n)
While i > 0:
    print(i)
    i // 2      # i를 2로 계속 나누어 가기 때문에, 밑이 2인 로그이다.
```