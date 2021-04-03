# -*- coding: utf-8 -*-
# @Time    : 2021-03-25 15:58
# @Author  : zxl
# @FileName: 040.py


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """


        ans = []
        candidates.sort()
        i = 0
        while i<len(candidates):

            num = candidates[i]
            if num>target:
                break
            if num == target:
                ans.append([num])
            else:
                sub_ans = self.combinationSum2(candidates[i+1:],target-num)
                for lst in sub_ans:
                    lst.insert(0,num)
                    ans.append(lst)
            i+=1
            while i<len(candidates) and candidates[i]==candidates[i-1]:
                i+=1
        return ans
obj = Solution()
candidates = [2,5,2,1,2]
target = 5
ans = obj.combinationSum2(candidates,target)
print(ans)
