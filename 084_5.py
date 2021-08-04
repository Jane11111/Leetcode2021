# -*- coding: utf-8 -*-
# @Time    : 2021-08-03 21:31
# @Author  : zxl
# @FileName: 084_5.py



class Solution:
    def largestRectangleArea(self, heights ) -> int:

        st = []

        ans = float('-inf')

        n = len(heights)

        for i in range(len(heights)):

            while len(st) and heights[i]<heights[st[-1]]:

                idx = st.pop()
                l = -1 if len(st) == 0 else st[-1]
                r = i
                area = heights[idx]*(r-l-1)
                ans = max(ans,area)
            st.append(i)

        while len(st):


            h = heights[st.pop()]
            l = -1 if len(st) == 0 else st[-1]
            r = n
            area = h*(r-l-1)
            ans = max(ans,area)
        return ans