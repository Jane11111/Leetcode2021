# -*- coding: utf-8 -*-
# @Time    : 2021-06-16 20:30
# @Author  : zxl
# @FileName: 446.py


# O(N^3)

class Solution:

    def recFind(self,used,dic,diff,last,last_idx,memo):

        if last_idx in memo and diff in memo[last_idx]:
            return memo[last_idx][diff]

        cur_num = last+diff

        if cur_num not in dic :
            return 0
        ans = 0
        for i in range(len(dic[cur_num])-1,-1,-1):
            idx = dic[cur_num][i]
            if idx<=last_idx:
                break
            if used[idx]:
                continue
            used[idx] = True
            # if last_idx == 1 and diff == 0:
            #     print('i am here')
            ans+=1+self.recFind(used,dic,diff,cur_num,idx,memo)
            # if last_idx == 1 and diff == 0:
            #     print('i am here')

            used[idx] = False
        if last_idx not in memo:
            memo[last_idx]= {}
        memo[last_idx][diff] = ans

        return ans



    def numberOfArithmeticSlices(self, nums ) -> int:

        n = len(nums)

        dic = {}
        for i in range(n):
            num = nums[i]
            if num not in dic:
                dic[num] = []
            dic[num].append(i)
        used = {i:False for i in range(n)}

        ans = 0
        for i in range(n):
            for j in range(i+1,n):
                ans += self.recFind(used,dic,nums[j]-nums[i],nums[j],j,{})
        return ans



obj = Solution()
nums = [2, 4, 6, 8, 10]

ans = obj.numberOfArithmeticSlices(nums)
print(ans)



