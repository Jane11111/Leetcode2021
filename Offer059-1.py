# -*- coding: utf-8 -*-
# @Time    : 2021-04-14 17:10
# @Author  : zxl
# @FileName: Offer059-1.py


class Solution:
    def maxSlidingWindow(self, nums , k )  :
        if len(nums) == 0:
            return []

        ans = []
        st = []
        for i in range(k-1):
            if len(st) == 0 or nums[i]<=st[-1]:
                st.append(nums[i])
            else:
                while len(st) > 0 and nums[i]>st[-1]:
                    st.pop()
                st.append(nums[i])
        # ans.append(st[0])
        for i in range(0,len(nums)-(k-1)):
            while len(st)> 0 and nums[i+k-1]>st[-1]:
                st.pop()
            st.append(nums[i+k-1])
            ans.append(st[0])
            if st[0] == nums[i]:
                st.pop(0)
        return ans


obj = Solution()
nums = [1,3,-1,-3,5,3,6,7]
k = 1
ans = obj.maxSlidingWindow(nums,k)
print(ans)