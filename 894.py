# -*- coding: utf-8 -*-
# @Time    : 2021-03-06 17:52
# @Author  : zxl
# @FileName: 894.py


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
import copy
class Solution(object):
    def recursiveConstruct(self,n,dic):

        res = []
        if n == 0:
            return res
        if n == 1:
            return [TreeNode()]
        if n%2 == 0:
            return res

        for i in range(1,n,2):
            if i in dic:
                left_lst = dic[i]
            else:
                left_lst = self.recursiveConstruct(i,dic)
                dic[i] = left_lst
            if n - 1 - i in dic:
                right_lst = dic[n-1-i]
            else:
                right_lst = self.recursiveConstruct(n - 1 - i,dic)

            if len(left_lst) == 0 or len(right_lst) == 0:
                continue
            for sub_left in left_lst:
                for sub_right in right_lst:
                    # new_left = copy.deepcopy(sub_left)
                    # new_right = copy.deepcopy(sub_right)
                    new_root = TreeNode(0, sub_left, sub_right)
                    res.append(new_root)
        return res

    def allPossibleFBT(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """

        res = self.recursiveConstruct(n,{})
        return res




n = 7
obj = Solution()
res = obj.allPossibleFBT(n)
for item in res:
    print(item)