"""A module for depth-first (in-order) traversal of trees."""

from typing import Iterable
from tree import T

def empty(stack):
    return len(stack) <= 0

def in_order(t: T | None) -> Iterable[int]:
    """In-order traversal of a tree.

    >>> tree = T(2, T(1, None, None), T(4, T(3, None, None), T(5, None, None)))
    >>> list(in_order(tree))
    [1, 2, 3, 4, 5]
    """
    if T is None:
        return []
    
    output = []
    stack = []
    node = t

    while not(empty(stack)) or node is not None:
        # If our node is None, it means that we have processed the left part, and we can append the solution
        if node is None:
            # Left part completed, we can process the parent
            node = stack.pop()
            output.append(node.val)
            node = node.right
        else:
            # Stack the parent node for later and process the left one
            stack.append(node)
            node = node.left

    return output

tree = T(2, T(1, None, None), T(4, T(3, None, None), T(5, None, None)))
print(list(in_order(tree)))
