# -*- coding: utf-8 -*-
# @Time    : 2021-04-08 10:37
# @Author  : zxl
# @FileName: 347_2.py


class Solution:
    def topKFrequent(self, nums, k):

        import heapq

        lst = []
        heapq.heappush(lst,3)
        heapq.heappush(lst,2)
        heapq.heappush(lst,5)
        return lst

obj = Solution()
ans = obj.topKFrequent([],3)
print(ans)