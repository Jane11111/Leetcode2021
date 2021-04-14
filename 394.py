# -*- coding: utf-8 -*-
# @Time    : 2021-04-06 17:11
# @Author  : zxl
# @FileName: 394.py


class Solution:
    def decodeString(self, s: str) -> str:
        ans = ''
        i = 0
        while i<len(s):
            if s[i] >= '0' and s[i] <= '9':
                j=i+1
                while j< len(s) and s[j] >='0' and s[j]<='9':
                    j+=1
                n = int(s[i:j])
                k = j
                c = 1
                while c!= 0:
                    k += 1
                    if s[k] == ']':
                        c-=1
                    if s[k] == '[':
                        c+=1

                sub_s = self.decodeString(s[j+1:k])
                for m in range(n):
                    ans += sub_s
                i = k+1
            else:
                ans += s[i]
                i+=1
        return ans

obj = Solution()
s = "abc3[cd]xyz"
ans = obj.decodeString(s)
print(ans)
