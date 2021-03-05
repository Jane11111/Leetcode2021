# -*- coding: utf-8 -*-
# @Time    : 2021-03-05 09:10
# @Author  : zxl
# @FileName: 109.py

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):

    def recursiveConstructTree(self,arr):
        if len(arr) == 0:
            return None
        elif len(arr) == 1:
            return TreeNode(arr[0])
        m = int(len(arr)/2)
        head = TreeNode(arr[m])
        left = self.recursiveConstructTree(arr[:m])
        right = self.recursiveConstructTree([] if m == len(arr)-1 else arr[m+1:])
        head.left = left
        head.right = right
        return head


    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        arr = []
        p = head
        while p != None:
            arr.append(p.val)
            p = p.next
        res = self.recursiveConstructTree(arr)
        return res
