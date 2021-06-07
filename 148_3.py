# -*- coding: utf-8 -*-
# @Time    : 2021-06-04 11:50
# @Author  : zxl
# @FileName: 148_3.py



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:


    def merge(self,pre,p1,p2,post):

        p = pre
        while p1 or p2:
            if not p1:
                p.next = p2
                p2 = p2.next
            elif not p2:
                p.next = p1
                p1 = p1.next
            else:
                if p1.val<p2.val:
                    p.next = p1
                    p1 = p1.next
                else:
                    p.next = p2
                    p2 = p2.next
            p = p.next
        p.next = post
        return p

    def pairMerge(self,pre,head,num):

        if head == None:
            return head

        p = head
        last = pre
        while p:

            cur = p
            count = 1
            while p and count<num:
                p = p.next
                count+=1
            if not p:
                return

            next = p.next
            p.next = None
            count = 1
            p = next
            while p and count<num:
                p = p.next
                count+=1
            tmp = None
            if p:
                tmp = p.next
                p.next = None

            last = self.merge(last,cur,next,tmp)
            p = tmp


    def sortList(self, head: ListNode) -> ListNode:

        new_head = ListNode()
        new_head.next = head
        num = 1
        count = 0
        p = head
        while p:
            count+=1
            p = p.next
        while num<count:
            self.pairMerge(new_head,new_head.next,num)
            num*=2
        return new_head.next


p1 = ListNode(4)
p2 = ListNode(2)
p3 = ListNode(1)
p4 = ListNode(3)
p1.next = p2
p2.next = p3
p3.next = p4
obj = Solution()
p = obj.sortList(p1)
print(p)