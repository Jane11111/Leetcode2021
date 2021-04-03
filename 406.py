# -*- coding: utf-8 -*-
# @Time    : 2021-03-09 21:16
# @Author  : zxl
# @FileName: 406.py


class Solution(object):


    def insertSort(self,people):
        # people[0] 从大到小, people[1]从小到大
        for i in range(len(people)):
            j = i-1
            tmp = people[i]
            while j>=0 and (people[j][0]<tmp[0] or (people[j][0]==tmp[0] and people[j][1]>tmp[1])):
                people[j+1] = people[j]
                j-=1
            people[j+1] = tmp
        return people

    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        sorted_people = self.insertSort(people)
        ans = [sorted_people[0]]
        for i in range(1,len(people)):
            item = people[i]
            idx = 0
            while idx<item[1]:
                idx+=1
            ans.insert(idx,item)
        return ans

obj = Solution()
people = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]
ans = obj.reconstructQueue(people)
print(ans)



