# -*- coding: utf-8 -*-
# @Time    : 2021-05-31 15:06
# @Author  : zxl
# @FileName: 164_2.py


class Solution:
    def maximumGap(self, nums ) -> int:

        if len(nums)<2:
            return 0

        min_val = float('inf')
        max_val = float('-inf')

        for num in nums:
            min_val = min(min_val,num)
            max_val = max(max_val,num)

        d = int((max_val-min_val)/(len(nums)-1))
        if d == 0:
            if max_val-min_val == 0:
                return 0
            else:
                d=1


        bucket_num = int((max_val-min_val)/d)+1

        buckets = [[float('inf'),float('-inf')] for i in range(bucket_num)]

        for num in nums:
            bucket_id = (num-min_val)//d

            buckets[bucket_id][0] = min(buckets[bucket_id][0],num)
            buckets[bucket_id][1] = max(buckets[bucket_id][1],num)

        i = 1
        ans = 0
        last_max = buckets[0][1]
        while i<len(buckets):

            while i<len(buckets) and buckets[i][0] == float('inf'):
                i+=1

            if i<len(buckets):
                ans = max(buckets[i][0]-last_max,ans)
                last_max = buckets[i][1]
                i+=1
        return ans

