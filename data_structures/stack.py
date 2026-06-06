"""Stack Implementation"""

from typing import Any, Optional


class Stack:
    """A simple stack (LIFO) data structure."""
    
    def __init__(self):
        self._items: list = []
    
    def push(self, item: Any) -> None:
        self._items.append(item)
    
    def pop(self) -> Any:
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self._items.pop()
    
    def peek(self) -> Any:
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self._items[-1]
    
    def is_empty(self) -> bool:
        return len(self._items) == 0
    
    def __len__(self) -> int:
        return len(self._items)
    
    def __repr__(self) -> str:
        return f"Stack({self._items})"


if __name__ == "__main__":
    s = Stack()
    for i in [1, 2, 3, 4, 5]:
        s.push(i)
    print(f"Stack: {s}")
    print(f"Peek: {s.peek()}")
    print(f"Pop: {s.pop()}")
    print(f"Stack after pop: {s}")
