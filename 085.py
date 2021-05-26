# -*- coding: utf-8 -*-
# @Time    : 2021-05-13 17:35
# @Author  : zxl
# @FileName: 085.py


class Solution:

    def getMaxMatrix(self,arr):

        n = len(arr)
        arr1 = [n for i in range(n)]
        arr2 = [-1 for i in range(n)]

        st1 = []
        for i in range(n):
            if len(st1) == 0 or arr[i]>=arr[st1[-1]]:
                st1.append(i)
            else:
                while len(st1) > 0 and arr[i]<arr[st1[-1]]:
                    arr1[st1.pop()] = i
                st1.append(i)
        st2 = []
        for i in range(n-1,-1,-1):
            if len(st2) == 0 or arr[i]>=arr[st2[-1]]:
                st2.append(i)
            else:
                while len(st2) > 0 and arr[i]<arr[st2[-1]]:
                    arr2[st2.pop()] = i
                st2.append(i)
        max_area = 0
        for i in range(n):
            max_area = max(max_area,arr[i]*(arr1[i]-arr2[i]-1))
        return max_area




    def maximalRectangle(self, matrix ) -> int:


        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])

        for j in range(n):
            count = 0
            for i in range(m):
                if matrix[i][j] == '1':
                    count+=1

                else:
                    count = 0
                matrix[i][j] = count

        max_area = 0
        for i in range(m):

            area = self.getMaxMatrix(matrix[i])
            max_area = max(max_area,area)
        return max_area


matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
obj = Solution()
ans = obj.maximalRectangle(matrix)
print(ans)