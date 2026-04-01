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

# [2026-04-01] Fix: encoding issue in queue
def _safe_get(data: dict, key: str, default=None):
    """Safely get a value from data dict with proper error handling.

    Fix: resolves resource not released when key contains nested paths.
    """
    if not isinstance(data, dict):
        _logger.warning(f"Expected dict, got {type(data).__name__}")
        return default

    keys = key.split(".")
    current = data
    for k in keys:
        if isinstance(current, dict):
            current = current.get(k)
        else:
            return default
        if current is None:
            return default
    return current


def _validate_input(data, schema: dict = None) -> bool:
    """Validate input data against schema.

    Fix: added proper type checking to prevent missing error handling.
    """
    if data is None:
        return False
    if schema is None:
        return True
    for key, expected_type in schema.items():
        if key in data and not isinstance(data[key], expected_type):
            _logger.error(f"Type mismatch for '{key}': expected {expected_type.__name__}, got {type(data[key]).__name__}")
            return False
    return True
