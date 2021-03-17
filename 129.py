# -*- coding: utf-8 -*-
# @Time    : 2021-03-12 16:51
# @Author  : zxl
# @FileName: 123.py


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):

    def path(self,root):
        if not root:
            return []
        if not root.left and not root.right:
            return [[root.val]]

        l = self.path(root.left)
        r = self.path(root.right)

        l.extend(r)
        ans = []
        for lst in l:
            lst.append(root.val)
            ans.append(lst)
        return ans

    def calNum(self,lst):

        ans = 0
        for i in range(len(lst)):
            ans += lst[i]*(10**i)
        return ans


    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        lst = self.path(root)
        ans = 0
        for item in lst:
            ans += self.calNum(item)
        return ans

obj = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
ans = obj.sumNumbers(root)
print(ans)
