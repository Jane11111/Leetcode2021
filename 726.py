# -*- coding: utf-8 -*-
# @Time    : 2021-05-25 13:20
# @Author  : zxl
# @FileName: 726.py

class Solution:

    def recCount(self,s,base,dic):

        if len(s) == 0:
            return
        i = 0
        if s[0] == '(':
            left_num = 1
            i+=1
            while left_num!=0 :
                if s[i] == '(':
                    left_num+=1
                elif s[i] == ')':
                    left_num-=1
                i+=1

            sub_s = s[1:i-1]
            count = ''
            while i<len(s) and s[i]>='0' and s[i]<='9':
                count+=s[i]
                i+=1
            if len(count) == 0:
                count = '1'
            self.recCount(sub_s,base*int(count),dic)
        else:

            atom = s[i]
            i+=1
            if i<len(s) and s[i] >='a' and s[i]<='z': #元素名字是两个字母
                atom += s[i]
                i+=1

            count = ''
            while i<len(s) and s[i]>='0' and s[i]<='9':
                count+=s[i]
                i+=1
            if atom not in dic:
                dic[atom] = 0

            if len(count) == 0:
                count = '1'
            dic[atom] += int(count)*base

        self.recCount(s[i:],base,dic)

    def countOfAtoms(self, formula: str) -> str:

        dic = {}
        base = 1
        self.recCount(formula,base,dic)
        lst = [[x,y] for x,y in dic.items()]
        lst.sort()
        ans = ''
        for atom,count in lst:
            ans += atom
            if count >1:
                ans += str(count)
        return ans

obj = Solution()
formula = 'K4(ON(SO3)2)2'
ans = obj.countOfAtoms(formula)
print(ans)
