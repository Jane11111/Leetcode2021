# -*- coding: utf-8 -*-
# @Time    : 2021-03-27 20:39
# @Author  : zxl
# @FileName: 135.py


class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        l1 = [0 for i in range(n)]
        l2 = [0 for i in range(n)]

        for i in range(1,n):
            if ratings[i]>ratings[i-1]:
                l1[i] = l1[i-1]+1
        for i in range(n-2,-1,-1):
            if ratings[i] > ratings[i+1]:
                l2[i] = l2[i+1]+1

        l3 = [max(l1[i],l2[i]) for i in range(n)]

        return sum(l3) + n

obj = Solution()
ratings = [1,3,2,2,1]
ans = obj.candy(ratings)
print(ans)
