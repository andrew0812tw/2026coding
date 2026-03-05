class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums) # 陣列的大小
        k = 0 # 要宣告K 一開始在最左邊待合
        for i in range(N): #把 nums[i] 逐一檢查
            if nums[i] != 0:
                nums[k] = nums[i] #左邊nums[k] 右邊nums[i]
                k += 1 # k 換下一個位置
        for i in range(k,N): # 剩下的格子
            nums[i] = 0 #全部補0
