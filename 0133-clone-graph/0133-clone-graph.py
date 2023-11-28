"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def __init__(self):
        self.mapOfNodes = {}
    
    def cloneGraph(self, node: 'Optional[Node]') -> 'Optional[Node]':
        if node is None:
            return None

        if node.val in self.mapOfNodes:
            return self.mapOfNodes[node.val]

        self.mapOfNodes[node.val] = Node(node.val, [])
        for neighb in node.neighbors:
            cloned_neighb = self.cloneGraph(neighb)
            self.mapOfNodes[node.val].neighbors.append(cloned_neighb)

        return self.mapOfNodes[node.val]
        
        # out = []
        # numNodes = len(mapOfNodes)
        # for i in mapOfNodes.keys():
        #     out.append([j if j in mapOfNodes[i].neighbors else 0 for j in range(numNodes)])
        # return out
        
            