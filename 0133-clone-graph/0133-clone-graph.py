"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    
    def cloneGraph(self, node: 'Optional[Node]', mapOfNodes=None) -> 'Optional[Node]':
        if node is None:
            return None

        if mapOfNodes is None:
            mapOfNodes = {}

        if node.val in mapOfNodes:
            return mapOfNodes[node.val]

        mapOfNodes[node.val] = Node(node.val, [])
        for neighb in node.neighbors:
            cloned_neighb = self.cloneGraph(neighb, mapOfNodes)
            mapOfNodes[node.val].neighbors.append(cloned_neighb)

        return mapOfNodes[node.val]
        
        # out = []
        # numNodes = len(mapOfNodes)
        # for i in mapOfNodes.keys():
        #     out.append([j if j in mapOfNodes[i].neighbors else 0 for j in range(numNodes)])
        # return out
        
            