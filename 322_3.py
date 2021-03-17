# -*- coding: utf-8 -*-
# @Time    : 2021-03-17 15:04
# @Author  : zxl
# @FileName: 322_3.py
# deque & set 572
# lst & set 636
# lst & dic 784

class Solution(object):

    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        from collections import deque
        lst = [amount]
        step = 0
        visited = {}
        while len(lst) > 0 :
            step += 1
            n = len(lst)
            for i in range(n):
                v = lst.pop(0)
                if v == 0:
                    return step-1
                for coin in coins:
                    if v-coin == 0:
                        return step
                    elif v-coin < 0:
                        continue
                    else:
                        if v-coin not in visited:
                            lst.append(v-coin)
                            visited[v-coin] = True

        return -1


# class Solution:
#     def coinChange(self, coins, amount)  :
#         from collections import deque
#         queue = deque([amount])
#         step = 0
#         visited = set()
#         while queue:
#             n = len(queue)
#             for _ in range(n):
#                 tmp = queue.pop()
#                 if tmp == 0:
#                     return step
#                 for coin in coins:
#                     if tmp >= coin and tmp - coin not in visited:
#                         visited.add(tmp - coin)
#                         queue.appendleft(tmp - coin)
#             step += 1
#         return -1

obj = Solution()
coins = [1,2,5]
amount = 11
ans = obj.coinChange(coins,amount)
print(ans)