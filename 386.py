# -*- coding: utf-8 -*-
# @Time    : 2021-06-22 19:37
# @Author  : zxl
# @FileName: 386.py


#TODO Wrong Answer

class Solution:

    def calNum(self,n):

        base = 0
        while n:
            base+=1
            n//=10
        return base


    def recFind(self,n,dic,s):
        if n in dic:
            return dic[n]


        if n<10:
            dic[n] = [str(i) for i in range(s,n+1)]
            if s == 0:
                dic[n].insert(0,'')
            return dic[n]

        base = self.calNum(n)
        new_n = n%(10**(base-1))

        lst1 = self.recFind(10**(base-1)-1,dic,0)

        lst2 = self.recFind(new_n,dic,0)
        if base == 2:
            lst3 = ['']
        else:
            lst3 = self.recFind(10**(base-2)-1,dic,0)

        h = n//(10**(base-1))

        ans = []
        for i in range(s,h):
            for item in lst1:
                ans.append(str(i)+item)

        for item in lst2:
            ans.append(str(h)+item)
        for i in range(h+1 ,10):
            for item in lst3:
                ans.append(str(i)+item)
        if s == 0:
            ans.insert(0,'')
        dic[n] = ans
        return dic[n]



    def lexicalOrder(self, n: int) :
        dic = {}

        ans = self.recFind(n,dic,1)
        lst = [int(item) for item in ans]
        return lst

obj =Solution()
n = 201
ans = obj.lexicalOrder(n)
print(len(ans))
print(ans)



