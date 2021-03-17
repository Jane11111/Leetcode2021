# -*- coding: utf-8 -*-
# @Time    : 2021-03-15 15:03
# @Author  : zxl
# @FileName: 096.py


class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """

        arr = [0 for i in range(n+1)]
        arr[0] = 1
        arr[1] = 1
        for i in range(2,n+1):
            max_val = 0

            for j in range(1,i+1):
                left_node = j-1
                right_node = i-j
                tree_num = arr[left_node] *arr[right_node]
                max_val +=tree_num
            arr[i] = max_val



        return arr[n]


obj = Solution()
n = 2
ans = obj.numTrees(n)
print(ans)
