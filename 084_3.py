# -*- coding: utf-8 -*-
# @Time    : 2021-05-30 13:49
# @Author  : zxl
# @FileName: 084_3.py



class Solution:
    def largestRectangleArea(self, heights ) -> int:


        st = []
        ans = 0

        for i in range(len(heights)):
            height = heights[i]

            while len(st)>0 and height<heights[st[-1]]:

                h = heights[st.pop()]
                if len(st)>0:
                    l = st[-1]
                else:
                    l = -1
                area = h*(i-l-1)
                ans = max(ans,area)
            st.append(i)
        while len(st)>0:

            h = heights[st.pop()]
            if len(st) > 0:
                l = st[-1]
            else:
                l = -1
            r = len(heights)
            area = h*(r-l-1)
            ans = max(ans,area)

        return ans
