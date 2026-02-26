# week01-2.py 學習計畫 Array/String 第一題
# Leetcode 1768. Merge Strings Alternately
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = "" #答案寫在 ans 裡
        N1, N2 = len(word1), len(word2)
        i,j=0,0
        while i<N1 or j<N2: #只要任一樣還有剩
            if i<N1: ans+=word1[j]
            if j<N2: ans+=word2[j]
            i,j=i+1,j+1
        return ans


