# -*- coding: utf-8 -*-
# @Time    : 2021-05-14 13:33
# @Author  : zxl
# @FileName: 239_2.py



class Solution:
    def maxSlidingWindow(self, nums , k: int) :



        st = []
        for i in range(k-1):
            while len(st)>0 and nums[i]>st[-1]:
                st.pop()
            st.append(nums[i])

        ans = []
        for i in range(k-1,len(nums)):

            while len(st)>0 and nums[i]>st[-1]:
                st.pop()
            st.append(nums[i])
            if i-k>=0 and st[0] == nums[i-k]:
                st.pop(0)
            ans.append(st[0])
        return ans



