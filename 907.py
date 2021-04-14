# -*- coding: utf-8 -*-
# @Time    : 2021-04-07 09:32
# @Author  : zxl
# @FileName: 907.py

class Solution:
    def sumSubarrayMins(self, arr) :

        n = len(arr)
        lst1 = []
        arr1 = [n-1 for i in range(n)]

        lst2 = []
        arr2 = [0 for i in range(n)]

        for i in range(n):
            if len(lst1) == 0 or arr[i]>=arr[lst1[-1]]:
                lst1.append(i)
            else:
                while len(lst1)>0 and arr[i]<arr[lst1[-1]]:
                    arr1[lst1[-1]] = i-1
                    lst1.pop()
                lst1.append(i)

            if len(lst2) == 0 or arr[n-i-1]>arr[lst2[-1]]:
                lst2.append(n-i-1)
            else:
                while len(lst2)>0 and arr[n-i-1]<=arr[lst2[-1]]:
                    arr2[lst2[-1]] = n-i-1+1
                    lst2.pop()
                lst2.append(n-i-1)

        count = 0
        # dic = {}
        for i in range(n):
            l = (i-arr2[i]+1)*(arr1[i]-i+1)
            # if arr[i] in dic:
            #     if arr[i-1] == arr[i]:
            #         l = arr1[i]-i+1
            #     else:
            #         l-=(dic[arr[i]]+1)
            # else:
            #     dic[arr[i]] = 0
            # dic[arr[i]]+=1

            count += l*arr[i]
            count %= (10**9+7)
        return count

obj = Solution()
arr=[36,74,84,92,17,68,97,6,68,85]

ans = obj.sumSubarrayMins(arr)
print(ans)



