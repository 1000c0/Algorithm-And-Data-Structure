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

        self.data = data
        self.next = None
