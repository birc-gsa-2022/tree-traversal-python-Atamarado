"""Module for representing trees."""

from __future__ import annotations
from dataclasses import dataclass


@dataclass
class T:
    """A node in a tree. Leaves are None"""
    val: int
    left: T | None
    right: T | None
