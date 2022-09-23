"""A module for breadth-first traversal of trees."""

from collections import deque
from typing import Iterable
from tree import T
from collections import deque

def bf_order(t: T | None) -> Iterable[int]:
    """Breadth-first traversal of a tree.

    >>> tree = T(2, T(1, None, None), T(4, T(3, None, None), T(5, None, None)))
    >>> list(bf_order(tree))
    [2, 1, 4, 3, 5]
    """
    queue = deque([t])
    output = []

    while queue:
        node = queue.popleft()
        if node is not None:
            output.append(node.val)
            queue.append(node.left)
            queue.append(node.right)

    return output

if __name__ == "__main__":
    tree = T(2, T(1, None, None), T(4, T(3, None, None), T(5, None, None)))
    print(list(bf_order(tree)))