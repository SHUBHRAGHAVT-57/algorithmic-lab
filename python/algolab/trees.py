"""Binary tree algorithms."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class TreeNode:
    """A binary tree node with an integer value and optional children."""

    value: int
    left: TreeNode | None = None
    right: TreeNode | None = None


def inorder_values(root: TreeNode | None) -> list[int]:
    """Visit a finite acyclic tree in left, root, right order. O(n) time, O(h) auxiliary space."""
    values: list[int] = []
    stack: list[TreeNode] = []
    current = root
    while current is not None or stack:
        while current is not None:
            stack.append(current)
            current = current.left
        current = stack.pop()
        values.append(current.value)
        current = current.right
    return values
