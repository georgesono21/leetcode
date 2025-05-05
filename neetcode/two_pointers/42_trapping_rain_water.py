class Solution:
    def trap(self, height: List[int]) -> int:

        """
        explanation: the brute force approach would be to iterate through the array
        and for each index i, calculate the max_left and max_right. then, we would
        calculate the water that can be trapped at that index i by taking the min
        of the two and subtracting the height at that index. this would be O(n^2)
        time and O(1) space. however, we can optimize this to O(n) time and O(n)
        space by using two arrays to store the max_left and max_right for each index.
        we can then iterate through the array again and calculate the water that can
        be trapped at each index by taking the min of the two arrays and subtracting
        the height at that index. this would be O(n) time and O(n) space.
        """

        max_right = [0 for i in range(len(height))]
        max_left = [0 for i in range(len(height))]

        total_water = 0

        for i in range(1, len(height)):
            max_height_left = max(max_left[i - 1], height[i - 1])
            max_left[i] = max_height_left

        for i in range(len(height) - 2, -1, -1):
            max_height_right = max(max_right[i + 1], height[i + 1])
            max_right[i] = max_height_right

        print(max_left, max_right)
        for i in range(len(height)):
            water = max(0, min(max_left[i], max_right[i]) - height[i])
            total_water += water

        return total_water

        return 0
# O(n) time, O(n) space

class Solution:
    def trap(self, height: List[int]) -> int:
        """
        explanation: from the O(n) implementation, we know that each position in the array
        needs a max_left and max_right to calculate the water that we can trap at an index i.
        so the two pointer approach takes advantage of the fact that we only need the minimum
        of the two. therefore, by starting on both ends of the array, if the max left on the
        left pointer is less than the max right on the right pointer, this means that for that
        index i, the water trapped at that height would be max_left - height[i]. w.r.t updating
        our pointers, if max_left is less than max_right, we would calculate the water at tha
        index and then increment the pointer by 1, (if it was right, then it would be -1)
        """

        # O(n) time, O(1) space
        l, r = 0, len(height) - 1

        max_left, max_right = height[0], height[-1]
        total_water = 0
        while l < r:
            if max_left < max_right:
                l += 1
                total_water += max(0, min(max_left, max_right) - height[l])
                max_left = max(height[l], max_left)
            else:
                r -= 1
                total_water += max(0, min(max_left, max_right) - height[r])
                max_right = max(height[r], max_right)

        return total_water
