# -*- coding: utf-8 -*-
# @Time    : 2021-04-02 13:16
# @Author  : zxl
# @FileName: 881.py


class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """

        people.sort()
        i = 0
        j = len(people) -1
        count = 0
        visited = [False for i in range(len(people))]
        while i<j and people[i]< limit:
            if people[i]+people[j]<=limit:
                count+=1
                visited[i] = True
                visited[j] = True
                i+=1
                j-=1
            else:
                j-=1
        for i in range(len(people)):
            if not visited[i]:
                count+=1
        return count

obj = Solution()
people = [1,2]
limit = 3
ans = obj.numRescueBoats(people,limit)
print(ans)




