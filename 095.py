# -*- coding: utf-8 -*-
# @Time    : 2021-03-15 15:11
# @Author  : zxl
# @FileName: 095.py


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):

    def recursiveConstruct(self,i,j):
        if i>j:
            return [None]
        if i==j:
            return [TreeNode(i)]

        ans = []
        for k in range(i,j+1):
            left_lst = self.recursiveConstruct(i,k-1)
            right_lst = self.recursiveConstruct(k+1,j)
            for p1 in left_lst:
                for p2 in right_lst:
                    root = TreeNode(k)
                    root.left = p1
                    root.right = p2
                    ans.append(root)
        return ans


    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """

        ans = self.recursiveConstruct(1,n)
        return ans

obj = Solution()
n = 3
ans = obj.generateTrees(n)
print(len(ans))
print(ans)

