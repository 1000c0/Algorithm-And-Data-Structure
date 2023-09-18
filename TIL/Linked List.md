## Linked List란?
- 각 노드가 데이터와 포인터를 가지고 한 줄로 연결되어 있는 방식으로 데이터를 저장하는 자료 구조

## Linked List의 특징
- Node : data part와 link part로 구성
- data를 linear-order하게(순서대로) memory 주소기반으로 연결
- 메모리 공간을 확보하지 않고, 데이터를 연결
- insertion과 deletion 등의 연산에 강점을 가짐

## 연속적인 데이터를 저장하는 법
- Array : 메모리 공간이 고정됨(fixed) -> flexibility가 고정됨
- List : 큰 data를 다루기에 적합X
  - 미리 공간을 확보해서 꽉차면 새로운 공간을 찾아 복붙하기 때문.
  - fixed size이지만 내부 구현으로 flexible하게 보이는 것
    #
    ### Array vs List
    - 100만개의 고정된 큰 데이터인 경우 : Array
    - 100개의 고정되지 않은 데이터인 경우 : List

## Code Example
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
a = Node(11)
b = Node(52)
c = Node(18)
a.next = b
b.next = c
b = None
c = None

print(a)  # <__main__.Node object at 0x10291c760> 
print(a.next)  # <__main__.Node object at 0x10291c520>
print(a.next.next)  # <__main__.Node object at 0x10291c490>
## a가 가르키는 주소를 출력 
print(a.next.data)  # 52
print(a.next.next.data)  # 18
```