# -*- coding: utf-8 -*-
# @Time    : 2021-04-02 19:38
# @Author  : zxl
# @FileName: 1769_2.py


class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """

        n = len(boxes)
        count = 0
        left_items = [0 for i in range(n)]

        init_val = 0

        for i in range(n):
            left_items[i]  = count
            if boxes[i] == '1':
                count += 1
                init_val += i

        dp = [0 for i in range(n)]
        dp[0] = init_val

        for i in range(1,n):

            right_item = count - left_items[i]
            if boxes[i] == 1:
                right_item-=1

            dp[i] = dp[i-1] + left_items[i]-right_item
        return dp

obj = Solution()
boxes = "110"
ans = obj.minOperations(boxes)
print(ans)










