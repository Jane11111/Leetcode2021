# -*- coding: utf-8 -*-
# @Time    : 2021-07-05 15:26
# @Author  : zxl
# @FileName: Shopee.py


class Solution:
    def compressString(self, param) :

        ans = ''

        i = 0
        while i<len(param):

            c = param[i]
            ans+=c
            j = i
            while j<len(param) and param[j] == c:
                j+=1
            count = j-i
            if count>1:
                ans += str(count)
            i = j
        return ans

obj = Solution()
param = 'aabcccccaaa'
ans = obj.compressString(param)
print(ans)






