# -*- coding: utf-8 -*-
# @Author: Hanchen Wang
# @Date:   2020-11-24 04:56:54
# @Last Modified by:   Hanchen Wang
# @Last Modified time: 2020-11-24 09:53:47

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # @param node, a undirected graph node
        # @return a undirected graph node
        if node is None:
            return None

        head = Node(node.val)
        nodeDict = {node.val: head}  # {node val: node Class}
        stack = [node]  # a list of node, EnQueue
        
        ''' == Vanilla BFS == '''
        while stack:
            top = stack.pop()  # pop the last element, DeQueue
            cnode = nodeDict[top.val] # current node
            
            for n in top.neighbors:
                if n.val not in nodeDict:
                    nodeDict[n.val] = Node(n.val)
                    stack.append(n)  # EnQueue
                cnode.neighbors.append(nodeDict[n.val])
        return head


    # hash table and BFS
    # O(n) time complexity, O(n) space

    def cloneGraph_Alt(self, node: 'Node') -> 'Node':

        if node is None:
            return None

        visited = set()
        que = collections.deque()
        nodes = {}
        que.append(node)
        visited.add(node)

        idx = 0
        while idx != len(que):
            curr = que[idx]
            idx += 1
            nodes[curr] = Node(curr.val)
            for node in curr.neighbors:
                if node not in visited:
                    visited.add(node)
                    que.append(node)
        start_node = None
        for node in que:
            curr = nodes[node]
            for neighbor in node.neighbors:
                curr.neighbors.append(nodes[neighbor])
            if start_node == None:
                start_node = curr
        return start_node
