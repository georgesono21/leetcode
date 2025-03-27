class Solution:
    def maxArea(self, height: List[int]) -> int:

        """
        intuition:
        use left and right pointers, to hold the most water, we would want to 
        preserve the highest wall height we have, so for whenever we have the 
        height of left is smaller than the right, we move our left pointer and
        keep our right wall the same (vice versa)
        """
        l = 0
        r = len(height)-1

        maxArea = 0
        while l < r:

            maxArea = max(maxArea, min(height[l],height[r])*(r-l))

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        #time O(n)
        return maxArea
