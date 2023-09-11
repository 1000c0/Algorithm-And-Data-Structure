## abstact data type(추상 자료형)이란?
- 컴퓨터 과학에서 자료들과 그 자료들에 대한 연산들을 명기한 것.
- 구현 방법을 명시하고 있지 않다는 점이 자료 구조와의 차이점이다.

## code example
```python
class List:
    def __init__(self):
        self.list = [] self.pos = 0
        self.size = 0
    
    def append(self, element):
        self.list.append(element)
        self.size += 1
    
    def length(self):
        return self.size

    def find(self, element):
        for i in range(self.size):
            if self.list[i] == element:
                return i
            return False
    
    def insert(self, element, after):
        insert_pos = self.find(after)
        if insert_pos:
            self.list.insert(insert_pos + 1, element)
            self.size += 1
            return True
        return False
    
    def remove(self, element):
        found_at = self.find(element)
        if found_at:
            del self.list[found_at]
            self.size -= 1
            return True
        return False
```
```python
class BaseClass(object):
    def __init__(self):
        super(BaseClass, self).__init__()
    
    def do_something(self):
        raise NotImplementedError(self.__class__.__name__ +'.try_something') # 에러 발생시키는 것

class SubClass(BaseClass):
    def do_something(self):
        print (self.__class__.__name__ + ' trying something!')

SubClass().do_something()
BaseClass().do_something()
```