# -*- coding: utf-8 -*-
# @Time    : 2021-06-29 20:01
# @Author  : zxl
# @FileName: 282_2.py

# O(4^N)

class Solution:



    def recFind(self,num,s,idx,target,pre_op,pre_num,val):

        if idx == len(num):
            if val == target :
                return [s]
        ans = []
        for i in range(idx,len(num)):
            cur_s = num[idx:i+1]
            if len(cur_s)>1 and cur_s[0] == '0':
                break

            if idx == 0:
                new_s = cur_s
                lst = self.recFind(num,new_s,i+1,target,pre_op,int(cur_s),int(cur_s))
                ans.extend(lst)
            else:
                new_s = s+'+'+cur_s
                new_val = val+int(cur_s)
                lst1 = self.recFind(num,new_s,i+1,target,'+',int(cur_s),new_val )

                new_s = s+'-'+cur_s
                new_val = val-int(cur_s)
                lst2 = self.recFind(num,new_s,i+1,target,'-',int(cur_s),new_val)

                new_s = s+'*'+cur_s
                if pre_op == '+':
                    new_val = val-pre_num + pre_num*int(cur_s)
                else:
                    new_val = val+pre_num - pre_num*(int(cur_s))
                lst3 = self.recFind(num,new_s,i+1,target,pre_op,pre_num*int(cur_s),new_val)
                ans.extend(lst1)
                ans.extend(lst2)
                ans.extend(lst3)
        return ans




    def addOperators(self, num: str, target: int):

        ans = self.recFind(num,'',0,target,'+',0,0)
        return ans
obj = Solution()
num = '105'
target = 5
ans = obj.addOperators(num,target)
print(ans)

