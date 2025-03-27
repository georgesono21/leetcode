class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        targets = dict()

        for i, v in enumerate(nums):
            if target - v in targets:
                return i, targets[target - v]
            else:
                targets[v] = i

        # time: O(n) , space: O(n)
