class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        #intuition: converge from both ends and check if left and right are equal to each other. we have to keep skipping indexes where chars are not alphabets,

        l = 0
        r = len(s)-1

        while (l < r):

            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            
            if s[l].lower() != s[r].lower():
                return False
            r -= 1
            l += 1

        return True

            