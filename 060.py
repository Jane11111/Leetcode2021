# -*- coding: utf-8 -*-
# @Time    : 2021-04-28 16:05
# @Author  : zxl
# @FileName: 060.py

class Solution:
    def getPermutation(self, n: int, k: int) -> str:

        i = 2
        lst = [1]
        while i<=n:
            lst.insert(0,i*lst[0])
            i+=1


        num_lst = [i for i in range(1,1+n)]

        ans = []

        i = 0
        while i<n:
            if lst[i]>k:
                ans.append(num_lst.pop(0))
                i+=1
            elif lst[i] == k:
                while len(num_lst)>0:
                    ans.append(num_lst.pop(-1))
                break
            else:
                num_lst.insert(0,ans.pop(-1))
                idx = k//lst[i]
                k = k % lst[i]
                if k >0:
                    ans.append(num_lst.pop(idx))
                else:
                    idx-=1
                    ans.append(num_lst.pop(idx))
                    while len(num_lst)>0:
                        ans.append(num_lst.pop(-1))
                    break

        s = ''
        for num in ans:
            s+=str(num)
        return s


obj = Solution()
n = 3
k = 6
ans = obj.getPermutation(n,k)
print(ans)

