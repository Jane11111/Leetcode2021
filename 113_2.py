# -*- coding: utf-8 -*-
# @Time    : 2021-06-07 11:07
# @Author  : zxl
# @FileName: 113_2.py



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def recSum(self,root,sum_val,targetSum,lst,ans):
        if not root:
            return

        if not root.left and not root.right:
            if sum_val+root.val == targetSum:
                lst.append(root.val)
                ans.append([x for x in lst])
            return

        if root.left:
            lst.append(root.val)
            self.recSum(root.left,sum_val+root.val,targetSum,lst,ans)
            lst.pop( )
        if root.right:
            lst.append(root.val)
            self.recSum(root.right,sum_val+root.val,targetSum,lst,ans)
            lst.pop( )


    def pathSum(self, root: TreeNode, targetSum: int)  :

        lst = []
        ans = []
        self.recSum(root,0,targetSum,lst,ans)
        return ans

