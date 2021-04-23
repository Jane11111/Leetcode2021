# -*- coding: utf-8 -*-
# @Time    : 2021-04-22 10:41
# @Author  : zxl
# @FileName: 230.py


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
import random
class Solution:



    def MaxHeapify(self,p):
        min_p = p
        min_dir = 0
        if p.left and p.left.val > min_p.val:
            min_p = p.left
            min_dir = 1

        if p.right and p.right.val > min_p.val:
            min_p = p.right
            min_dir = 2

        if min_p == p:
            return min_p

        new_head = min_p
        tmp1 = new_head.left
        tmp2 = new_head.right

        if min_dir == 1:
            new_head.right = p.right

            p.left = tmp1
            p.right = tmp2
            new_head.left = self.MaxHeapify(p)
        else:
            new_head.left = p.left

            p.left = tmp1
            p.right = tmp2
            new_head.right = self.MaxHeapify(p)

        return min_p
    def InsertMaxHeap(self,root,p):
        if root == None:
            return p
        n = random.random()
        if n<0.5:
            p.right = root
            p.left = root.left
            root.left = None
        else:
            p.left = root
            p.right = root.right
            root.right = None
        return self.MaxHeapify(p)


    def kthSmallest(self, root: TreeNode, k: int) -> int:
        max_heap = None
        min_heap = None

        count = 0
        Q = [root] if root else []

        while len(Q)>0:

            l = len(Q)
            i = 0
            while i<l:
                p = Q.pop(0)
                i+=1

                if p.left:
                    Q.append(p.left)
                if p.right:
                    Q.append(p.right)
                p.left = None
                p.right = None
                if count<k:
                    max_heap = self.InsertMaxHeap(max_heap,p)
                    count +=1
                else:
                    if p.val<max_heap.val:

                        tmp = max_heap
                        p.left = tmp.left
                        p.right = tmp.right
                        max_heap = self.MaxHeapify(p)
        return max_heap.val
