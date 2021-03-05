# -*- coding: utf-8 -*-
# @Time    : 2021-03-05 17:19
# @Author  : zxl
# @FileName: 725.py


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        count = 0
        p = root
        while p:
            count += 1
            p = p.next
        res = []
        m = count%k
        n = int (count/k)

        p = root
        for i in range(k):
            num = n+1 if i < m else n
            if num == 0:
                res.append(None)
            else:
                res.append(p)
                for j in range(num-1):
                    p = p.next
                tmp = p.next
                p.next = None
                p = tmp
        return res

