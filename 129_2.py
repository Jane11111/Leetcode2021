# -*- coding: utf-8 -*-
# @Time    : 2021-03-12 17:07
# @Author  : zxl
# @FileName: 129_2.py

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):

    def recursiveSum(self,root,base):

        if not root:
            return 0
        if not root.left and not root.right:
            return 10*base + root.val

        l = self.recursiveSum(root.left,base*10+root.val)
        r = self.recursiveSum(root.right,base*10+root.val)

        return l+r




    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        ans = self.recursiveSum(root,0)
        return ans

obj = Solution()
root = TreeNode(4)
root.left = TreeNode(9)
root.right = TreeNode(0)
root.left.left = TreeNode(5)
root.left.right = TreeNode(1)
ans = obj.sumNumbers(root)
print(ans)

