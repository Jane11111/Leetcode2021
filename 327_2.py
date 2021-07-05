# -*- coding: utf-8 -*-
# @Time    : 2021-07-02 15:50
# @Author  : zxl
# @FileName: 327_2.py

class TreeNode():

    def __init__(self,val=0,count=0,le_count=0,left=None,right=None):
        self.val = val
        self.count = count
        self.le_count = le_count
        self.left = left
        self.right = right

#TODO 非平衡二叉树 超时

class Solution:
    def updateNode(self,root,val):
        if not root:
            return
        if root.val>val:
            root.le_count+=1
        self.updateNode(root.left,val)
        self.updateNode(root.right,val)

    def insertNode(self,root,val):
        p = self.findSmallNode(root,val)
        self.updateNode(root,val)# 把le count更新
        if not p:
            p = root
            while p.left:
                p = p.left
            p.left = TreeNode(val,1,1)
        else:
            if p.val == val:
                p.count+=1
                p.le_count += 1
                return
            else:
                tmp = TreeNode(val,1,p.le_count+1)
                tmp.right = p.right
                p.right = tmp

    def findSmallNode(self,root,val):
        if root == None or root.val==val:
            return root
        if root.val<val:
            p = self.findSmallNode(root.right,val)
            if not p:
                return root
            else:
                return p
        else:
            return self.findSmallNode(root.left,val)
    def findLargeNode(self,root,val):
        if root == None or root.val == val:
            return root
        if root.val<val:
            return self.findLargeNode(root.right,val)
        else:
            p = self.findLargeNode(root.left,val)
            if not p:
                return root
            return p


    def countRangeSum(self, nums, lower: int, upper: int) -> int:

        pre_sums = 0
        ans = 0
        root = TreeNode(0,1,1)
        for num in nums:
            pre_sums+=num
            r = pre_sums-lower
            l = pre_sums-upper

            p1 = self.findLargeNode(root,l)
            p2 = self.findSmallNode(root,r)

            if p1 and p2:

                ans+=(p2.le_count-p1.le_count+p1.count)
            self.insertNode(root, pre_sums)
        return ans

obj = Solution()
nums = [0]
lower = 0
upper = 0
ans = obj.countRangeSum(nums,lower,upper)
print(ans)


