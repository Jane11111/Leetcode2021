# -*- coding: utf-8 -*-
# @Time    : 2021-03-11 22:20
# @Author  : zxl
# @FileName: 074.py


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        if len(matrix) == 0:
            return False

        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == target:
                    return True
                else:
                    continue
        return False

obj = Solution()
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
ans = obj.searchMatrix(matrix,target)
print(ans)