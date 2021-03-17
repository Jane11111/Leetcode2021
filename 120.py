# -*- coding: utf-8 -*-
# @Time    : 2021-03-15 15:23
# @Author  : zxl
# @FileName: 120.py


class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """

        for i in range(1,len(triangle)):
            cur_lst = triangle[i]

            for j in range(len(cur_lst)):

                if j == 0:
                    triangle[i][j] = triangle[i][j] + triangle[i - 1][j]
                elif j<len(cur_lst)-1:
                    triangle[i][j] = triangle[i][j]+ min(triangle[i-1][j],triangle[i-1][j-1])
                else:
                    triangle[i][j] = triangle[i][j]+triangle[i-1][j-1]

        return min(triangle[-1])

obj= Solution()
triangle = [[-1],[3,2],[-3,1,-1]]
ans = obj.minimumTotal(triangle)
print(ans)