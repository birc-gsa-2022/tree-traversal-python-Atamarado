"""Module for representing trees."""

from __future__ import annotations
from dataclasses import dataclass


@dataclass
class T:
    """A node in a tree. Leaves are None"""
    val: int
    left: T | None
    right: T | None
    thread: T | None

    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
        self.thread = None
