class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        """
        intuition: kadanes algorithim

        reccurence relation: dp[i] = max(dp[i-1] + nums[i], nums[i])

        optimize as we only keep track of only previous, so we need two variables max

        """
        maxSum = nums[0]
        runningSum = 0
        
        for i, num in enumerate(nums):
            
            
            if runningSum < 0:
                runningSum = 0
            runningSum += num

            maxSum = max(maxSum, runningSum)

        
        return maxSum