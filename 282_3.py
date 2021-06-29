# -*- coding: utf-8 -*-
# @Time    : 2021-06-29 20:38
# @Author  : zxl
# @FileName: 282_3.py

# O(N*4^N)


class Solution:

    def cal(self,s):
        i = 0
        while i <len(s) and s[i].isdigit():
            i+=1
        pre_op ='+'
        pre_val = int(s[:i])
        val = int(s[:i])

        while i<len(s):
            op = s[i]
            j = i+1
            while j<len(s) and s[j].isdigit():
                j+=1
            num = int(s[i+1:j])

            if op == '+':
                val += num
                pre_op = '+'
                pre_val = num
            elif op == '-':
                val -= num
                pre_op = '-'
                pre_val = num
            else:
                if pre_op == '+':
                    val = val-pre_val + pre_val*num
                    pre_val = pre_val*num
                else:
                    val = val+pre_val -pre_val*num
                    pre_val = pre_val*num

            i = j
        return val



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
num = '105'
target = 5
ans = obj.addOperators(num,target)
print(ans)