# -*- coding: utf-8 -*-
# @Time    : 2021-03-26 14:34
# @Author  : zxl
# @FileName: 140.py


class Solution(object):

    def recursiveBreak(self,s,wordDict):
        if len(s) == 0:
            return [[]]

        sentences = []
        for i in range(1,len(s)+1):
            if s[:i] in wordDict:
                sub_sentences = self.recursiveBreak(s[i:],wordDict)
                for sub_sentence in sub_sentences:
                    sub_sentence.insert(0,s[:i])
                    sentences.append(sub_sentence)
        return sentences



    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        sentences = self.recursiveBreak(s,wordDict)
        ans = []
        for sentence in sentences:
            ans.append(' '.join(sentence))
        return ans

obj = Solution()
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
sentences = obj.wordBreak(s,wordDict)
print(sentences)


