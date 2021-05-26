# -*- coding: utf-8 -*-
# @Time    : 2021-05-11 19:13
# @Author  : zxl
# @FileName: 394_3.py



class Solution:
    def decodeString(self, s: str) -> str:


        new_s = ''

        i = 0

        while i<len(s):

            if s[i]>='0' and s[i]<='9':
                j = i+1
                while j<len(s) and s[j]>='0' and s[j]<='9':
                    j+=1
                num = int(s[i:j])
                left_count = 1
                k = j
                while left_count!=0:
                    k+=1
                    if s[k] == ']':
                        left_count-=1
                    elif s[k] == '[':
                        left_count +=1
                cur_str = self.decodeString(s[j+1:k])
                while num:
                    new_s += cur_str
                    num-=1

                i = k+1

            else:
                new_s += s[i]
                i+=1
        return new_s

obj = Solution()
s = "2[abc]3[cd]ef"
ans = obj.decodeString(s)
print(ans)








