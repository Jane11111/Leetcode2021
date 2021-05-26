# -*- coding: utf-8 -*-
# @Time    : 2021-05-13 19:59
# @Author  : zxl
# @FileName: 085_2.py



class Solution:

    def getMaxMatrix(self,arr):
        arr.append(0)

        n = len(arr)
        max_area = 0
        st = []
        for i in range(n):

            while len(st)>0 and arr[i]<arr[st[-1]]:

                idx = st.pop()
                if len(st)==0:
                    l = -1
                else:
                    l = st[-1]
                max_area = max(max_area,arr[idx]*(i-l-1))
            st.append(i)
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