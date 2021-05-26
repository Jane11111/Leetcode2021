# -*- coding: utf-8 -*-
# @Time    : 2021-05-16 21:04
# @Author  : zxl
# @FileName: 128.py


class Solution:
    def longestConsecutive(self, nums ) -> int:

        dic = {}
        for num in nums:
            dic[num] = True

        count_dic = {}
        for num in nums:
            if num in count_dic:
                continue

            if num+1 in count_dic:
                count_dic[num] = count_dic[num+1]+1
            else:
                count = 1
                cur_num = num+1
                while True:
                    if cur_num in dic:
                        if cur_num in count_dic:
                            count+= count_dic[cur_num]
                            break
                        else:
                            count+=1
                            cur_num+=1
                    else:
                        break
                count_dic[num] = count

                count-=1
                for tmp_num in range(num+1,num+count):
                    if tmp_num in count_dic:
                        break
                    count_dic[tmp_num] = count
                    count-=1
        ans = 0
        for k,v in count_dic.items():
            ans = max(ans,v)
        return ans

obj = Solution()
nums = [0,3,7,2,5,8,4,6,0,1,-1]
ans = obj.longestConsecutive(nums)
print(ans)







