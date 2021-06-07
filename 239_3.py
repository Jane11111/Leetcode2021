# -*- coding: utf-8 -*-
# @Time    : 2021-06-04 14:10
# @Author  : zxl
# @FileName: 239_3.py


class Solution:
    def maxSlidingWindow(self, nums , k: int) :


        st = []
        for i in range(0,k-1):
            while len(st)>0 and st[-1]<nums[i]:
                st.pop()
            st.append(nums[i])
        ans = []
        for i in range(k-1,len(nums)):
            while len(st)>0 and st[-1]<nums[i]:
                st.pop()
            st.append(nums[i])
            ans.append(st[0])
            if st[0] == nums[i-k+1]:
                st.pop(0)
        return ans
