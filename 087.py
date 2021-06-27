# -*- coding: utf-8 -*-
# @Time    : 2021-06-15 16:32
# @Author  : zxl
# @FileName: 087.py


# TODO 超时

class Solution:

    def recFind(self,s1,s2 ,visited):


        if len(s1) <=1 :
            return s1 == s2
        if s1 == s2:
            return True


        if s1 in visited and s2 in visited[s1]:
            return visited[s1][s2]
        if s1 not in visited:
            visited[s1] = {}

        dic = {}
        not_cover = 0
        for i in range(len(s1)):

            if s1[i] != s2[i]:
                if s1[i] not in dic or dic[s1[i]] == 0:
                    dic[s1[i]]= 0
                    not_cover+=1
                dic[s1[i]]-=1
                if dic[s1[i]] == 0:
                    not_cover -=1

                if s2[i] not in dic or dic[s2[i]] == 0:
                    dic[s2[i]] = 0
                    not_cover+=1
                dic[s2[i]]+=1
                if dic[s2[i]] == 0:
                    not_cover -=1

            if not_cover == 0:
                if i == len(s1)-1:
                    break

                f1 = self.recFind(s1[:i+1],s2[:i+1] ,visited)
                f2 = self.recFind(s1[i+1:],s2[i+1:],visited )

                if f1 and f2:
                    visited[s1][s2] = True
                    return True

        # if len(s1) == len(s2) :
        #     print('i am here')
        dic = {}
        not_cover = 0
        n = len(s2)-1
        for i in range(len(s1)):

            if s1[i] != s2[n-i]:
                if s1[i] not in dic or dic[s1[i]] == 0:
                    dic[s1[i]] = 0
                    not_cover += 1
                dic[s1[i]] -= 1
                if dic[s1[i]] == 0:
                    not_cover -= 1

                if s2[n-i] not in dic or dic[s2[n-i]] == 0:
                    dic[s2[n-i]] = 0
                    not_cover += 1
                dic[s2[n-i]] += 1
                if dic[s2[n-i]] == 0:
                    not_cover -= 1

            if not_cover == 0:
                if i == len(s1) - 1:
                    visited[s1][s2] = False
                    return False

                f1 = self.recFind(s1[:i + 1], s2[n-i:],visited)
                f2 = self.recFind(s1[i + 1:], s2[:n-i],visited)

                if f1 and f2:
                    visited[s1][s2] = True
                    return True
        visited[s1][s2] = False
        return False


    def isScramble(self, s1: str, s2: str) -> bool:
        return self.recFind(s1,s2,{})



obj = Solution()
s1 = "abcd"
s2 = "bdac"

ans = obj.isScramble(s1,s2)
print(ans)


