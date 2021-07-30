# -*- coding: utf-8 -*-
# @Time    : 2021-07-26 16:44
# @Author  : zxl
# @FileName: 085_3.py


class Solution:

    def calRec(self,heights):
        ans = 0

        st = []

        for i in range(len(heights)):

            while st and heights[i] < heights[st[-1]]:
                idx = st.pop()
                ans = max(ans, (i - 1 - (st[-1] if st else -1)) * heights[idx])
            st.append(i)

        n = len(heights)
        for i in range(len(st)):
            idx = st[i]
            ans = max(ans, (n - 1 - (st[i - 1] if i > 0 else -1)) * heights[idx])
        return ans

    def maximalRectangle(self, matrix ) -> int:


        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        ans = 0
        dp = [0 for i in range(n)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j]== '1':
                    dp[j] +=1
                else:
                    dp[j] = 0
            area = self.calRec(dp)
            ans = max(area,ans)
        return ans

