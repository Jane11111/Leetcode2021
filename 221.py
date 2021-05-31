# -*- coding: utf-8 -*-
# @Time    : 2021-05-26 21:00
# @Author  : zxl
# @FileName: 221.py


class Solution:

    def findMaxSquare(self,arr):

        st = []
        max_square = 0
        for idx in range(len(arr)):
            while len(st)>0 and arr[idx]<arr[st[-1]]:

                cur_idx = st.pop()
                if len(st)>0:
                    left = st[-1]
                else:
                    left = -1
                max_square = max(max_square, (min(idx-left-1,arr[cur_idx]))**2)
            st.append(idx)

        while len(st)>0:
            cur_idx = st.pop()
            if len(st) > 0:
                left = st[-1]
            else:
                left = -1
            max_square = max(max_square,(min(len(arr)-left-1,arr[cur_idx]))**2)

        return max_square



    def maximalSquare(self, matrix ) -> int:


        m = len(matrix)
        n = len(matrix[0])

        for j in range(n):
            count = 0
            for i in range(m):
                if matrix[i][j] == '0':
                    matrix[i][j] = 0
                    count = 0
                else:
                    count+=1
                    matrix[i][j] = count
        ans = 0
        for i in range(m):
            max_square = self.findMaxSquare(matrix[i])
            ans = max(ans,max_square)
        return ans




