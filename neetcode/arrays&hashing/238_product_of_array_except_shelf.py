class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        intuition:
        we know that a product except itself for an index i, would be product(0,A[i-1])
        * product(A[i+1],n), so to do this in O(n) time, we would need to precalculate
        the prefix and suffix from 0~n. So, for each index i, we know that the suffix product
        (the product on the right side) would be equal to suffix[i+1] and the prefix product
        (product on the left side) would be equal to prefix[i-1]. Then, we just multiply them
        both to get the product excluding the value at index i.

        to optimize it to use O(1) memory (excluding the result array), we would use the result
        array as a prefix array. there's other stuff to but its kinda complicated

        """

        # O(n) time O(n) memory

        prefix, suffix, res = list(), list(), list()
        for i in range(len(nums)):
            prefix.append(0)
            suffix.append(0)
            res.append(0)

        prefix[0] = nums[0]
        suffix[-1] = nums[-1]

        for i in range(1, len(nums)):
            prefix[i] = nums[i] * prefix[i - 1]

        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = nums[i] * suffix[i + 1]

        res[0] = suffix[1]
        res[-1] = prefix[-2]

        for i in range(1, len(nums) - 1):
            res[i] = prefix[i - 1] * suffix[i + 1]
        return res

        # Optimized:

        # use prefix in new return array
        # runningPostFix * index in new return array

        arr = list()
        runningPreFix = 1
        for i in range(len(nums)):
            arr.append(runningPreFix)
            runningPreFix *= nums[i]

        runningPostFix = 1
        for i in range(len(nums) - 1, -1, -1):
            arr[i] = arr[i] * runningPostFix
            runningPostFix *= nums[i]

        return arr
