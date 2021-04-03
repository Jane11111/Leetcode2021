# -*- coding: utf-8 -*-
# @Time    : 2021-04-02 11:34
# @Author  : zxl
# @FileName: 738.py


class Solution(object):
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """

        s = str(N)

        lst = [int(i) for i in s]

        ans = [lst[0]]
        for i in range(1,len(lst)):
            if lst[i]<ans[-1]:
                j = len(ans)-1
                while j-1>=0 and ans[j]-1 < ans[j-1]:
                    j-=1
                ans[j]-=1
                for k in range(j+1,len(ans)):
                    ans[k] = 9
                while len(ans) < len(lst):
                    ans.append(9)
                break

            else:
                ans.append(lst[i])

        new_s = ''
        for n in ans:
            new_s += str(n)
        return int(new_s)
obj = Solution()
N = 200
ans= obj.monotoneIncreasingDigits(N)
print(ans)



