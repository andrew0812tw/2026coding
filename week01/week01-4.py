# week01-4.py 學習計畫 Array/String 第三題
# 1431. Kids With the Greatest Number of Candies
# 你給額外的extraCandies 後, 小朋友手上的糖果,會不會是最多的？
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        #(庫存)
        ans = [] #答案的True
        best = max(candies)
        for candie in candies:
            if candie +extraCandies >=best:ans.append(True)
            else: ans.append(False)
        return ans
