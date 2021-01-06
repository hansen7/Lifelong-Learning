# -*- coding: utf-8 -*-
# @Author: Hanchen Wang
# @Date:   2021-01-06 13:00:32
# @Last Modified by:   Hanchen Wang
# @Last Modified time: 2021-01-06 13:25:35


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def findTarget1(self, root: TreeNode, k: int) -> bool:

        """first convert the tree into a set, then search, suboptimal"""
        
        self.val_set = set()
        self.traverse(root)

        for n in self.val_set:
            if k - n != n and k - n in self.val_set:
                return True
        return False

    def traverse(self, root):
        if not root: return None
        self.val_set.add(root.val)
        self.traverse(root.left)
        self.traverse(root.right)

    def findTarget2(self, root: TreeNoode, k: int) -> bool:
        """search within the tree, more efficient
        NOT WORKING, failed case: [2,0,3,-4,1], -1"""

        self.k = k
        self.root = root
        return self.findNumber(root)

    def findNumber(self, root):
        if not root: return False
        node, n, = self.root, self.k - self.root.val
        if n != root.val:
            while node:
                if node.val == n: return True
                elif n > node.val: node = node.right
                else: node = node.left
        return self.findNumber(root.left) or self.findNumber(root.right)

    def findTarget3(self, root: TreeNoode, k: int) -> bool:

        """a more inclusive one of findTarget2()"""
        #TODO: 2dev
