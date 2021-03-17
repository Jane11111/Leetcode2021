# -*- coding: utf-8 -*-
# @Time    : 2021-03-16 21:53
# @Author  : zxl
# @FileName: 072.py


class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1) + 1
        n = len(word2) + 1
        arr = []
        for i in range(m):
            arr.append([0 for i in range(n)])
        for i in range(m):
            arr[i][0] = i

        for i in range(n):
            arr[0][i] = i

        for i in range(1,m):
            for j in range(1,n):
                if word1[i-1] == word2[j-1]:
                    arr[i][j] = arr[i-1][j-1]
                else:
                    arr[i][j] = min([arr[i-1][j]+1,arr[i][j-1]+1,arr[i-1][j-1]+1])

        return arr[m-1][n-1]

word1 = "intention"
word2 = "execution"
obj = Solution()
ans = obj.minDistance(word1,word2)
print(ans)