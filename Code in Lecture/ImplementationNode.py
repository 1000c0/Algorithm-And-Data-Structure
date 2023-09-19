from typing import Any


class Node:
    """
    A class to represent a Node for an explanation of data structure.

    ...

    Attributes
    ----------
    data : Any
        data that user store on Node instance
    next: Node
        object connected to the next node in a linked list.
    """

    def __init__(self, data: Any = None, next: "Node" = None) -> None:
        """
        Args:
            data (Any, oprional): data that user store on Node instance
            next (Node, optional): object connected to the next node in a linked list

        Returns:
            None
        """

        self._data = data  # _ information hiding -> 외부에서 접근하지 못하게 하기 위함
        self._next = None

    @property
    def data(self):
        """data that user store on Node instance"""
        return self._data

    @property
    def next(self):
        """data that user store on Node instance"""
        return self._next

    @data.setter
    def data(self, value: Any) -> None:
        self._data = value

    @next.setter
    def next(self, node: "Node") -> None:
        self._next = node

    def __str__(self) -> str:
        return_str = (
            f"I have a data : {self._data}\n" + f"I hava a node : {id(self._next)}"
        )
        return return_str

    def __repr__(self) -> str:
        return_str = f"Node({self._data})"
        return return_str
        # self._next 로 할 경우
        # I have a data : 2
        # I hava a node : I have a data : 52
        # I hava a node : I have a data : 18
        # I hava a node : None

    def __add__(self, other) -> None:
        self._next = other


class Vector:
    def __init__(self, *args):
        self.args = args

    def __add__(self, other):
        a = [arg1 + arg2 for arg1, arg2 in zip(self.args, other.args)]

    def __repr__(self):
        return self.__class__.__name__ + str(self.args)


v1 = Vector(1, 4, 8, 9)
v2 = Vector(5, 3, 2, 1)


class LinkedListBag(object):
    """_summary_

    Args:
        object (_type_): _description_
    """

    def __init__(self, first_node: Node = None) -> None:
        super().__init__()
        self._head = first_node
        self._tail = first_node
        if first_node is None:
            self.size = 0
        else:
            self.size = self._count(self)

    def __contains__(self, target: int):
        cur_node = self.head
        while cur_node is not None:
            if cur_node.data == target:
                return True
            else:
                return False

    def _count(self) -> int:
        counter = 0
        cur_node = self._head
        while cur_node is not None:
            counter += 1
            cur_node = cur_node.next
        return counter

    def append(self, new_node: Node) -> bool:  # O(1) -> tail 끝에 붙히기 때문
        try:
            if self.size == 0:
                self._head = new_node
                self._tail = new_node
            else:
                self._tail.next = new_node
                self._tail = new_node
            self.size += 1
            return True
        except Exception as e:
            print(e)
            return False

    def insert(self, new_node: Node, index_number: int) -> bool:
        index_counter = 0
        cur_node = self._head

        if index_number == 0:
            new_node.next = self._head
            self._head = new_node
            self.size += 1
            return True

        while cur_node is not None:
            if index_number == index_counter:
                pred_node.next = new_node
                new_node.next = cur_node
                self.size += 1
                return True
            else:
                pred_node = cur_node
                cur_node = cur_node.next
                index_counter += 1
        return False

    def remove(self, target_value: int) -> bool:
        cur_node = self._head

        while cur_node is not None:
            if cur_node == target_value:
                pred_node.next = cur_node.next
                del cur_node
                self.size -= 1
                return True
            else:
                pred_node = cur_node
                cur_node = cur_node.next
        return False

    def __len__(self) -> int:
        return self.size

    def __repr__(self) -> str:
        cur_node = self.head
        if self.size == 0:
            return None
        return_str = ""
        while cur_node is not None:
            return_str += f" {cur_node.data} -> "
            cur_node = cur_node.next
        return_str += f"End of Linked List"
        return return_str

    def __iter__(self):
        return _BagIterator(self._head)

    @property
    def head(self) -> Node:
        return self._head


class _BagIterator:
    def __init__(self, head_node) -> None:
        self._cur_node = head_node

    def __iter__(self):
        return self

    def __next__(self):
        if self._cur_node is None:
            raise StopIteration
        else:
            node = self._cur_node
            self._cur_node = self._cur_node.next
            return node
