"""A module for depth-first (in-order) traversal of trees."""

from typing import Iterable
from tree import T

def in_order(t: T | None) -> Iterable[int]:
    """In-order traversal of a tree.

    >>> tree = T(2, T(1, None, None), T(4, T(3, None, None), T(5, None, None)))
    >>> list(in_order(tree))
    [1, 2, 3, 4, 5]
    """
    
    output = []
    stack = []
    node = t

    while stack or node:
        # If our node is None, it means that we have processed the left part, and we can append the solution
        if not(node):
            # Left part completed, we can process the parent
            node = stack.pop()
            output.append(node.val)
            node = node.right
        else:
            # Stack the parent node for later and process the left one
            stack.append(node)
            node = node.left

    return output

def thread_tree(t: T | None):
    root = t
    node = t
    next = None

    if node.left:
        next = node
        node = node.left

    while node:
        if node is root:
            node = node.right
        elif node.left:
            if node.thread:
                if node.right:
                    next = node.thread
                    node.thread = None
                    node = node.right
                else:
                    node = node.thread
            else:
                node.thread = next
                next = node
                node = node.left
        elif node.right:
            node = node.right
        else:
            node.thread = next
            node = next
            next = None

def in_order_thread(t: T | None) -> Iterable [int]:
    output = []

    # Find the first node
    node = t
    while node.left:
        node = node.left

    # Inorder
    while node:
        output.append(node)
        if node.right:
            node = node.right
        else:
            node = node.thread
    
    return output


if __name__ == "__main__":
    tree = T(2, T(1, None, None), T(4, T(3, None, None), T(5, None, None)))
    thread_tree(tree)
    print(list(in_order_thread(tree)))
