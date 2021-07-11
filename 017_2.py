# -*- coding: utf-8 -*-
# @Time    : 2021-07-07 15:53
# @Author  : zxl
# @FileName: 017_2.py


class Solution:

    def recFind(self,dic,digits,idx,s,ans):

        if len(s) == len(digits):
            ans.append(s)
            return

        for c in dic[int(digits[idx])]:
            self.recFind(dic,digits,idx+1,s+c,ans)



    def letterCombinations(self, digits: str)  :

        if len(digits) == 0:
            return []

        dic = {2:['a','b','c'],
               3:['d','e','f'],
               4:['g','h','i'],
               5:['j','k','l'],
               6:['m','n','o'],
               7:['p','q','r','s'],
               8:['t','u','v'],
               9:['w','x','y','z']}
        ans = []
        self.recFind(dic,digits,0,'',ans)
        return ans

obj = Solution()
digits = '23'
ans = obj.letterCombinations(digits)
print(ans)
