# -*- coding: utf-8 -*-
# @Time    : 2021-03-09 21:49
# @Author  : zxl
# @FileName: 023.py



# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        root = ListNode()
        p = root

        while len(lists)!=0:

            cur_p = None
            cur_val = 100000
            i = 0
            idx = 0
            while i<len(lists):
                if lists[i] == None:
                    lists.pop(i)
                else:
                    if lists[i].val<cur_val:
                        cur_val = lists[i].val
                        cur_p = lists[i]
                        idx = i
                    i+=1
            if cur_p:
                p.next = cur_p
                p = p.next
                lists[idx] = lists[idx].next
        return root.next

obj = Solution()
p1 = ListNode(1)
p1.next = ListNode(4)
p1.next.next = ListNode(5)

p2 = ListNode(1)
p2.next = ListNode(3)
p2.next.next = ListNode(4)

p3 = ListNode(2)
p3.next = ListNode(6)

lists = [p1,p2,p3]
res = obj.mergeKLists(lists)
print(res)
