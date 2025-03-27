class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        """
        intuition: if we sort the array, then it is the case that we can loop from 0 and
        from i+1 to the end of the array, we run two sum 2 (where input array is sorted).
        two avoid dupicate pairs, we make sure to keep pushing left, right pointers, to make
        sure they're on unique elements and not the same as their previous. there is a hashset
        solution if you want to leave the array unsorted, but that is pretty hard to understand.
        """
        nums.sort()
        res = list()

        for i in range(len(nums)): #O(n)
            
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = len(nums)-1

            while l < r: #O(n)
                triplet = [nums[l], nums[r], nums[i]]
                if sum(triplet) == 0:
                    # print(i, l ,r)
                    res.append(triplet)
                
                if sum(triplet) > 0:
                    r -= 1
                    while nums[r] == nums[r+1] and l < r:
                        r -= 1
                else:
                    l+=1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
  

        #time: O(n^2) space: O(1) depends on sorting algo
        
        return res
                
