# -*- coding: utf-8 -*-
# @Time    : 2021-04-14 17:43
# @Author  : zxl
# @FileName: I1709.py


class Solution:
    def getKthMagicNumber(self, k: int) -> int:
        arr = [1,3,5,7]
        p3 = 1
        p5 = 2
        p7 = 3
        while len(arr)<k:
            v3 = arr[p3]*3
            v5 = arr[p5]*5
            v7 = arr[p7]*7
            min_val = min([v3,v5,v7])

            if min_val%v3 == 0:
                p3+=1
            if min_val%v5 == 0:
                p5+=1
            if min_val%v7 == 0:
                p7+=1
            arr.append(min_val)


        return arr[k-1]

obj = Solution()
k = 200
ans = obj.getKthMagicNumber(k)
print(ans)