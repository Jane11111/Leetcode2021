# -*- coding: utf-8 -*-
# @Time    : 2021-03-05 19:58
# @Author  : zxl
# @FileName: 1019.py


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """

        val_stack = []
        idx_stack = []
        res = []
        idx = 0
        p = head
        while p:
            # if len(val_stack) == 0:
            #     val_stack.append(p.val)
            #     idx_stack.append(idx)
            #     res.append(0)
            # else:
            while len(val_stack) != 0 and p.val > val_stack[len(val_stack)-1]:
                val_stack.pop()
                pos = idx_stack.pop()
                res[pos] = p.val
            val_stack.append(p.val)
            idx_stack.append(idx)
            res.append(0)

            p = p.next
            idx += 1
        return res
