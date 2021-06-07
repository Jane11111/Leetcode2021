# -*- coding: utf-8 -*-
# @Time    : 2021-06-07 11:26
# @Author  : zxl
# @FileName: 113_3.py





# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int):



        st = [root] if root else []

        sum_lst = [root.val] if root else []

        ans = []

        dic = {root:None}

        while len(st)>0:
            p = st.pop(0)
            sum_val = sum_lst.pop(0)


            if not p.left and not p.right and sum_val == targetSum:

                cur_lst = []
                while p :
                    cur_lst.insert(0,p.val)
                    p = dic[p]
                ans.append(cur_lst)
            else:
                if p.left:
                    dic[p.left] = p
                    st.append(p.left)
                    sum_lst.append(sum_val+p.left.val)
                if p.right:
                    dic[p.right] = p
                    st.append(p.right)
                    sum_lst.append(sum_val+p.right.val)
        return ans

