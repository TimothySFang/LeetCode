"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        graph_mapping = {}

        def dfs(curr_node):
            if not curr_node:
                return

            if curr_node in graph_mapping:
                return graph_mapping[curr_node]

            clone = Node(curr_node.val)
            graph_mapping[curr_node] = clone

            for neighbor in curr_node.neighbors:
                clone.neighbors.append(dfs(neighbor))

            return clone
        return dfs(node)
