# -*- coding: utf-8 -*-
# @Time    : 2021-04-25 15:52
# @Author  : zxl
# @FileName: Offer046.py


class Solution:

    def translate(self,lst ,i,dic):

        if i == len(lst):
            return 1
        if i in dic:
            return dic[i]
        num = lst[i]
        # c = chr(ord('a')+num)
        ans = self.translate(lst,i+1,dic)
        if num!=0 and i+1<len(lst) and num*10+lst[i+1]<26:
            num = num*10+lst[i+1]
            ans += self.translate(lst ,i+2,dic)
        dic[i] = ans
        return ans

    def translateNum(self, num: int) -> int:

        lst = []
        while num:
            lst.insert(0,num%10)
            num//=10

        ans = self.translate(lst ,0,{})
        return ans

obj = Solution()
num = 25
ans = obj.translateNum(num)
print(ans)