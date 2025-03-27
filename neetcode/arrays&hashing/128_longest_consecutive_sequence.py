class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        """
        try to find the "root" number, which is the number that doesn't have a number
        consecutively before it. once we have a root number, start a streak of 1, and keep
        increasing it by 1 and check if that number exists in nums and if it does, increment
        by one.
        """

        nums = set(nums)
        longest = 0
        for num in nums:
            if num-1 in nums:
                continue
            
            streak = 0
            while num in nums:
                num = num + 1
                streak += 1
            longest = max(longest,streak)
        
        return longest

        #O(n) time, O(1) space
