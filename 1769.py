# -*- coding: utf-8 -*-
# @Time    : 2021-04-02 19:29
# @Author  : zxl
# @FileName: 1769.py


class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """

        idx_lst = []
        for i in range(len(boxes)):
            if boxes[i] == '1':
                idx_lst.append(i)
        ans = [0 for i in range(len(boxes))]
        for i in range(len(boxes)):
            num = 0
            for k in idx_lst:
                num+=abs(k-i)
            ans[i] = num
        return ans

boxes = "001011"
obj = Solution()
ans = obj.minOperations(boxes)
print(ans)