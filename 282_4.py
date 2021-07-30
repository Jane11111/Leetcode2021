# -*- coding: utf-8 -*-
# @Time    : 2021-07-20 20:11
# @Author  : zxl
# @FileName: 282_4.py


class Solution:

    def recurSolve(self,s,idx,cur_val,last_op,last_val,target,eq,ans):

        if idx == len(s):
            if cur_val == target:
                ans.append(eq)
            return

        for i in range(idx,len(s)):

            subs = s[idx:i+1]
            if len(subs)>1 and subs[0] == '0':
                break
            num = int(s[idx:i+1])


            self.recurSolve(s,i+1,cur_val+num,'+',num,target,eq+'+'+str(num),ans)
            self.recurSolve(s,i+1,cur_val-num,'-',num,target,eq+'-'+str(num),ans)
            if last_op == '+':
                new_val = cur_val-last_val + last_val*num
                self.recurSolve(s,i+1,new_val,last_op,last_val*num,target,eq+'*'+str(num),ans)
            else:
                new_val = cur_val + last_val - last_val*num
                self.recurSolve(s, i + 1, new_val, last_op, last_val * num, target, eq + '*' + str(num), ans)




    def addOperators(self, num: str, target: int) :

        if len(num) == 0:
            return []

        ans = []
        for i in range(len(num)):
            subs = num[:i+1]
            if len(subs)>1 and subs[0] == '0':
                break
            cur_num = int(subs)
            self.recurSolve(num,i+1,cur_num,'+',cur_num,target,subs,ans)
        return ans

obj = Solution()
num = "3456237490"
target = 9191
ans = obj.addOperators(num,target)
print(ans)