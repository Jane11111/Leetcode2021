# -*- coding: utf-8 -*-
# @Time    : 2021-03-05 10:40
# @Author  : zxl
# @FileName: 148.py


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):

    def merge_sort(self,p1,p2):
        if p1 == p2:
            p1.next = None
            return p1

        count = 0

        p = p1
        while p != p2.next:
            count += 1
            p = p.next

        m = count // 2
        count  = 1
        p = p1
        while count < m:
            p = p.next
            count += 1
        if p.next == None:
            print('i am here')
        tmp = p.next
        l = self.merge_sort(p1,p)
        r = self.merge_sort(tmp,p2)
        head = self.merge(l,r)
        return head


    def merge(self,l,r):

        head = ListNode()
        p = head

        while l or r:
            if l == None:
                p.next = r
                r = None
            elif r == None:
                p.next = l
                l = None
            else:
                if l.val<r.val:
                    p.next = l
                    l = l.next
                else:
                    p.next = r
                    r = r.next
                p = p.next
        return head.next



    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head == None:
            return head
        p = head
        while p.next:
            p = p.next
        head = self.merge_sort(head,p)
        return head


head = ListNode(4)
head.next = ListNode(2)
head.next.next = ListNode(1)
head.next.next.next = ListNode(3)
obj = Solution()
p = obj.sortList(head)
print(p)