# -*- coding: utf-8 -*-
# @Author: Hanchen Wang
# @Date:   2020-11-24 04:56:54
# @Last Modified by:   Hanchen Wang
# @Last Modified time: 2020-11-24 07:08:56

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        result = self.inorderTra(root)
        
        for i in range(1, len(result)):
            if result[i] <= result[i-1]:
                return False
        return True


    def inorderTra(self, root):
        """ DFS """
        result = []
        if root is None:
            return result
        result += self.inorderTra(root.left)
        result.append(root.val)
        result += self.inorderTra(root.right)
        return result 

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        result = self.inorderTra(root)
        valid = True

        while valid:
            valid = self.OneDepthTree(root.left)

        for i in range(1, len(result)):
            if result[i] <= result[i-1]:
                return False
        return True

    def OneDepthTree(self, root: TreeNode) -> bool:
        if root is None:
            return True    
        if self.left is not None:
            if self.left > root:
                return False
        if self.right is not None:
            if self.right < root:
                return False
        return True
        
