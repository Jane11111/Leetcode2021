# -*- coding: utf-8 -*-
# @Time    : 2021-05-25 11:32
# @Author  : zxl
# @FileName: 129_3.py



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def recFind(self,root):
        if root == None:
            return [[]]
        if not root.left and not root.right:
            return [[root.val]]
        if root.left:
            l = self.recFind(root.left)
        else:
            l = []
        if root.right:
            r = self.recFind(root.right)
        else:
            r = []
        l.extend(r)

        ans = []
        for lst in l:
            lst.insert(0, root.val)
            ans.append(lst)
        return ans

    def lst2num(self,lst):
        num = 0
        base = 0
        for i in range(len(lst)-1,-1,-1):
            num += lst[i]*(10**base)
            base+=1
        return num

    def sumNumbers(self, root: TreeNode) -> int:


        lst = self.recFind(root)
        ans = 0

        for sub_lst in lst:
            ans+=self.lst2num(sub_lst)
        return ans


p1 = TreeNode(2)
p2 = TreeNode(1)
p3 = TreeNode(3)
p2.left = p1
p2.right = p3
obj = Solution()
ans = obj.sumNumbers(p2)
print(ans)