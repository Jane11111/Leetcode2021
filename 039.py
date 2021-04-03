# -*- coding: utf-8 -*-
# @Time    : 2021-03-25 15:27
# @Author  : zxl
# @FileName: 039.py


class Solution(object):


    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        candidates.sort()
        ans = []

        for i in range(len(candidates)):
            if candidates[i] > target:
                return ans
            num = candidates[i]
            for j in range(1,int(target//num)+1):
                if target-j*num<0:
                    break
                elif target-j*num == 0:
                    ans.append([num for k in range(j)])
                else:
                    sub_ans = self.combinationSum(candidates[i+1:],target-j*num)
                    for lst in sub_ans:
                        tmp = [num for k in range(j)]
                        tmp.extend(lst)
                        ans.append(tmp)
        return ans

obj = Solution()
candidates = [2,3,5]
target = 8
ans = obj.combinationSum(candidates,target)
print(ans)


