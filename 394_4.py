# -*- coding: utf-8 -*-
# @Time    : 2021-05-11 19:27
# @Author  : zxl
# @FileName: 394_4.py



class Solution:
    def decodeString(self, s: str) -> str:


        i = 0
        lst = []
        while i<len(s):
            if s[i] >= '0' and s[i] <= '9':

                j = i+1
                while j<len(s) and s[j]>='0' and s[j]<='9':
                    j+=1
                lst.append(int(s[i:j]))
                i=j
            elif s[i]>='a' and s[i] <='z':
                j = i+1
                while j<len(s) and s[j]>='a' and s[j]<='z':
                    j+=1
                if len(lst)>0 and type(lst[-1]) == type('a'):
                    lst[-1] += s[i:j]
                else:
                    lst.append(s[i:j])

                i = j
            elif s[i] == '[':
                i+=1
            else:
                cur_s = lst.pop()
                new_s =''
                num = lst.pop()
                while num :
                    new_s += cur_s
                    num-=1
                if len(lst)>0 and type(lst[-1]) == type('a'):
                    lst[-1]+=new_s
                else:
                    lst.append(new_s)
                i+=1
        return lst[-1]



obj = Solution()
s = "3[a]2[bc]"
ans = obj.decodeString(s)
print(ans)
