# -*- coding: utf-8 -*-
# @Time    : 2021-08-04 11:04
# @Author  : zxl
# @FileName: 087_5.py


class Solution:

    def recFind(self,s1,s2,dic):

        # if s1 == 'abcd' and s2 == 'abcd':
        #     print(' i am here')


        if s1 in dic and s2 in dic[s1]:
            return dic[s1][s2]
        if s1 not in dic:
            dic[s1] = {}

        if len(s1) == 1:
            dic[s1][s2] = s1 == s2
            return dic[s1][s2]

        not_cover = 0
        s1dic = {}
        s2dic = {}
        for i in range(len(s1)):

            if s1[i] not in s1dic:
                s1dic[s1[i]] = 0
            if s2[i] not in s2dic:
                s2dic[s2[i]] = 0



            # if s1dic[s1[i]] == 1:
            #     not_cover+=1

            if s1[i] == s2[i]:
                s1dic[s1[i]] +=1
                s2dic[s2[i]] +=1
            else:
                s1dic[s1[i]] +=1
                if (s1[i] not in s2dic and s1dic[s1[i]] == 1) or (s1[i]  in s2dic and s1dic[s1[i]]-s2dic[s1[i]]==1) :
                    not_cover += 1

                s2dic[s2[i]] += 1
                if (s2[i] not in s1dic and s2dic[s2[i]] == 1) or (s2[i]  in s1dic and s2dic[s2[i]] - s1dic[s2[i]] ==1):
                    not_cover += 1

                if s2[i] in s1dic and s2dic[s2[i]] == s1dic[s2[i]]:
                    not_cover-=1
                if s1[i]!=s2[i] and s1[i] in s2dic and s2dic[s1[i]] == s1dic[s1[i]]:
                    not_cover -=1

            # if s1 == 'abcdbdacbdac' and s2 == 'bdacabcdbdac' and i == 7:
            #     print('i am here')

            if not_cover == 0 and i!= len(s1)-1:
                f1 = self.recFind(s1[:i+1],s2[:i+1],dic)
                f2 = self.recFind(s1[i+1:],s2[i+1:],dic)
                if f1 and f2:
                    dic[s1][s2] = True
                    return True

        not_cover = 0
        s1dic = {}
        s2dic = {}
        n = len(s2)
        for i in range(len(s1)):

            if s1[i] not in s1dic:
                s1dic[s1[i]] = 0
            if s2[n-1-i] not in s2dic:
                s2dic[s2[n-1-i]] = 0

            if s1[i] == s2[n-1-i]:
                s1dic[s1[i]] += 1
                s2dic[s2[n-1-i]] += 1
            else:
                s1dic[s1[i]] += 1
                if (s1[i] not in s2dic and s1dic[s1[i]] == 1) or(s1[i]  in s2dic and s1dic[s1[i]] - s2dic[s1[i]] == 1):
                    not_cover += 1

                s2dic[s2[n-1-i]] += 1
                if (s2[n-1-i] not in s1dic and s2dic[s2[n-1-i]] == 1) or(s2[n-1-i]  in s1dic and s2dic[s2[n-1-i]] - s1dic[s2[n-1-i]] == 1):
                    not_cover += 1

                if s2[n-1-i] in s1dic and s2dic[s2[n-1-i]] == s1dic[s2[n-1-i]]:
                    not_cover -= 1
                if s1[i] in s2dic and s2dic[s1[i]] == s1dic[s1[i]]:
                    not_cover -= 1

            if not_cover == 0 and i != len(s1) - 1:
                f1 = self.recFind(s1[:i + 1], s2[n-1-i:], dic)
                f2 = self.recFind(s1[i + 1:], s2[:n-1-i], dic)
                if f1 and f2:
                    dic[s1][s2] = True
                    return True

        dic[s1][s2] = False
        return False

    def isScramble(self, s1: str, s2: str) -> bool:


        ans = self.recFind(s1,s2,{})
        return ans



obj = Solution()

s1 = "abcdbdacbdac"
s2 = "bdacabcdbdac"
ans = obj.isScramble(s1,s2)
print(ans)