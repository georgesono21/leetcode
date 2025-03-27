class Solution:
    def isValid(self, s: str) -> bool:
        
        syms = {")":"(", "}":"{", "]":"["}
        stack = list()

        for l in s:
            if l in syms:
                if not len(stack):
                    return False

                top = stack[-1]
                if syms[l] != top:
                    return False
                stack.pop(-1)
            else:
                stack.append(l)
        
        return len(stack) == 0

#time: O(n), space: O(n)