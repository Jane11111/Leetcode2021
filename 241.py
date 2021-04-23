# -*- coding: utf-8 -*-
# @Time    : 2021-04-22 20:08
# @Author  : zxl
# @FileName: 241.py


class Solution:

    def cal(self,lst,i,j,dic):

        if i == j:
            return [lst[i]]
        if str([i,j]) in dic:
            return dic[str([i,j])]
        ans = []
        for k in range(i+1,j,2):
            l = self.cal(lst,i,k-1,dic)
            r = self.cal(lst,k+1,j,dic)
            for n1 in l:
                for n2 in r:
                    if lst[k] == '+':
                        n = n1+n2
                    elif lst[k] == '-':
                        n = n1-n2
                    else:
                        n = n1*n2
                    ans.append(n)
        dic[str([i,j])] = ans
        return ans


    def diffWaysToCompute(self, expression )  :

        lst = []
        s = ''
        for i in range(len(expression)):
            c= expression[i]
            if c == '+' or c == '-' or c == '*':
                lst.append(int(s))
                lst.append(c)
                s = ''
            else:
                s+=c
        lst.append(int(s))

        ans = self.cal(lst,0,len(lst)-1,{})
        return ans

obj = Solution()
expression = "2-1-1"
ans = obj.diffWaysToCompute(expression)
print(ans)