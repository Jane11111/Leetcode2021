# -*- coding: utf-8 -*-
# @Time    : 2021-06-29 17:01
# @Author  : zxl
# @FileName: 282.py


#O(N*4^N)

class Solution:

    def cal(self,s):
        i = 0
        lst = []
        while i<len(s):
            j = i+1
            while j<len(s) and s[j].isdigit():
                j+=1
            num = s[i:j]
            lst.append(int(num))
            if len(lst)>=3 and lst[-2] == '*':
                n1  = lst.pop()
                lst.pop()
                n2 = lst.pop()
                lst.append(n1*n2)

            if j<len(s):
                lst.append(s[j])
            i=j+1
        v = lst[0]
        for i in range(1,len(lst),2):
            if lst[i] == '+':
                v+=lst[i+1]
            else:
                v-=lst[i+1]
        return v



    def recFind(self,num,new_s,idx):
        if idx == len(num):
            return [new_s]
        ans = []
        for i in range(idx,len(num)):
            if len(num[idx:i+1]) >1 and num[idx] == '0':
                break
            if idx == 0:
                cur_s = new_s + num[idx:i+1]
                lst = self.recFind(num,cur_s,i+1)
                ans.extend(lst)
            else:
                cur_s = new_s+'+'+num[idx:i+1]
                lst1 = self.recFind(num,cur_s,i+1)
                cur_s = new_s + '-' + num[idx:i + 1]
                lst2 = self.recFind(num, cur_s, i + 1)
                cur_s = new_s + '*' + num[idx:i + 1]
                lst3 = self.recFind(num, cur_s, i + 1)
                ans.extend(lst1 )
                ans.extend(lst2)
                ans.extend(lst3)
        return ans


    def addOperators(self, num: str, target: int) :
        ans = []


        lst = self.recFind(num,'',0)
        for s in lst:
            if len(s) == num:
                continue
            n = self.cal(s)
            if n == target:
                ans.append(s)
        return ans


obj = Solution()
num = '232'
target = 8
ans = obj.addOperators(num,target)
print(ans)
#
# s = '1*0*0+1'
# ans = obj.cal(s)
# print(ans)











