# -*- coding: utf-8 -*-
# @Time    : 2021-06-25 17:22
# @Author  : zxl
# @FileName: 433_3.py


# 双向BFS

class Solution:


    def minMutation(self, start: str, end: str, bank ) -> int:
        # TODO
        pass



obj = Solution()
start = "AAAACCCC"
end = "CCCCCCCC"
bank = ["AAAACCCA","AAACCCCA","AACCCCCA","AACCCCCC","ACCCCCCC","CCCCCCCC","AAACCCCC","AACCCCCC"]
ans = obj.minMutation(start,end,bank)
print(ans)
