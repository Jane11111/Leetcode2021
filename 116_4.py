# -*- coding: utf-8 -*-
# @Time    : 2021-07-28 10:56
# @Author  : zxl
# @FileName: 116_4.py



class Solution:

    def connect(self, root: 'Node') -> 'Node':


        if not root:
            return root
        p = root
        while p and p.left:

            tmp = p.left
            p.left.next = p.right

            while p.next:

                p.right.next = p.next.left
                p = p.next
                p.left.next = p.right

            p = tmp
        return root


