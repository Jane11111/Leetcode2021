# -*- coding: utf-8 -*-
# @Time    : 2021-06-30 17:52
# @Author  : zxl
# @FileName: 318.py


class Solution:





    def maxProduct(self, words ) -> int:

        word_dic = {}
        for word in words:
            arr = [0 for i in range(26)]
            for c in word:
                arr[ord(c)-ord('a')] = 1
            word_dic[word] = arr

        max_len = 0

        for i in range(len(words)):
            word1 = words[i]
            for j in range(i+1,len(words)):
                word2 = words[j]

                valid = True
                for k in range(26):
                    if word_dic[word1][k] == 1 and word_dic[word2][k] ==1:
                        valid = False
                        break
                if valid:
                    max_len = max(max_len,len(word1)*len(word2))
        return max_len


obj = Solution()

words = ["abcw","baz","foo","bar","xtfn","abcdef"]
ans = obj.maxProduct(words)
print(ans)