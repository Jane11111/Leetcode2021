# -*- coding: utf-8 -*-
# @Time    : 2021-04-06 20:49
# @Author  : zxl
# @FileName: 856.py

class Solution:
    def scoreOfParentheses(self, S: str) -> int:

        lst = []
        score = [0 for i in range(len(S))]
        arr = [-1 for i in range(len(S))]
        for i in range(len(S)):
            if S[i] == '(':
                lst.append(i)
            else:
                count = 0
                k = lst[-1] + 1
                while k<i:
                    count += score[k]
                    k = arr[k]+1
                if count == 0:
                    score[lst[-1]] = 1
                else:
                    score[lst[-1]] = count*2
                arr[lst[-1]] = i
                lst.pop()
        ans = 0
        i = 0
        while i<len(S):
            ans+=score[i]
            i = arr[i]+1
        return ans
obj = Solution()
S = "(()(()))"
ans = obj.scoreOfParentheses(S)
print(ans)


