# -*- coding: utf-8 -*-
# @Time    : 2021-07-26 16:33
# @Author  : zxl
# @FileName: 084_4.py


class Solution:
    def largestRectangleArea(self, heights ) -> int:



        ans = 0

        st = []

        for i in range(len(heights)):

            while st and heights[i]<heights[st[-1]]:
                idx = st.pop()
                ans = max(ans,(i-1-(st[-1]if st else -1))*heights[idx])
            st.append(i)

        n = len(heights)
        for i in range(len(st)):
            idx = st[i]
            ans = max(ans,(n-1-(st[i-1] if i>0 else -1))*heights[idx])
        return ans

obj = Solution()
heights = [2,4]
ans = obj.largestRectangleArea(heights)
print(ans)