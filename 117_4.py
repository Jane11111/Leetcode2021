# -*- coding: utf-8 -*-
# @Time    : 2021-07-28 11:23
# @Author  : zxl
# @FileName: 117_4.py


class Solution:

    def recConnect(self,cur,next): #将下一层进行connect

        if not cur.left and not cur.right:
            if next:
                self.recConnect(next,next.next)
            return

        if cur.left and cur.right:
            cur.left.next = cur.right
            last = cur.right
        elif not cur.left:
            last = cur.right
        else:
            last = cur.left

        while next and (not next.left and not next.right):
            next = next.next

        if not next:
            return
        last.next = (next.left if next.left else next.right)
        self.recConnect(next,next.next)


    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None

        self.recConnect(root,root.next)

        p = root
        last = None
        while not last and p:
            last = p.left
            if not last:
                last = p.right
                p = p.next
        self.connect(last)
        return root









