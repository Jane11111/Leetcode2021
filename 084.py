# -*- coding: utf-8 -*-
# @Time    : 2021-04-03 09:58
# @Author  : zxl
# @FileName: 084.py


class Solution:
    def largestRectangleArea(self, heights) :

        n = len(heights)

        r_lst = []
        r_arr = [-1 for i in range(n)]

        for i in range(n):
            if len(r_lst) == 0 or heights[i]>=heights[r_lst[-1]]:
                r_lst.append(i)
            else:
                while len(r_lst)>0 and heights[i]<heights[r_lst[-1]]:
                    r_arr[r_lst[-1]] = i-1
                    r_lst.pop(-1)
                r_lst.append(i)
        for i in range(n):
            if r_arr[i] ==-1:
                r_arr[i] = n-1

        l_lst = []
        l_arr = [-1 for i in range(n)]
        for i in range(n-1,-1,-1):
            if len(l_lst) == 0 or heights[i]>=heights[l_lst[-1]]:
                l_lst.append(i)
            else:
                while len(l_lst) > 0 and heights[i]<heights[l_lst[-1]]:
                    l_arr[l_lst[-1]] = i+1
                    l_lst.pop(-1)
                l_lst.append(i)
        for i in range(n):
            if l_arr[i] == -1:
                l_arr[i] = 0

        ans = 0
        for i in range(n):
            area = heights[i]*(r_arr[i]-l_arr[i]+1)
            ans = max(ans,area)
        return ans

obj = Solution()
heights = [2,1,5,6,2,3]
ans = obj.largestRectangleArea(heights)
print(ans)


