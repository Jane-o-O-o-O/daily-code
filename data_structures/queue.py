"""Queue Implementation"""

from typing import Any
from collections import deque


class Queue:
    """A simple queue (FIFO) data structure."""
    
    def __init__(self):
        self._items = deque()
    
    def enqueue(self, item: Any) -> None:
        self._items.append(item)
    
    def dequeue(self) -> Any:
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self._items.popleft()
    
    def front(self) -> Any:
        if self.is_empty():
            raise IndexError("Front of empty queue")
        return self._items[0]
    
    def is_empty(self) -> bool:
        return len(self._items) == 0
    
    def __len__(self) -> int:
        return len(self._items)
    
    def __repr__(self) -> str:
        return f"Queue({list(self._items)})"


if __name__ == "__main__":
    q = Queue()
    for i in [1, 2, 3, 4, 5]:
        q.enqueue(i)
    print(f"Queue: {q}")
    print(f"Front: {q.front()}")
    print(f"Dequeue: {q.dequeue()}")
    print(f"Queue after dequeue: {q}")
