class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # intuition: get counts of all chars from both strings and see if they're the same
        sDict = {}
        tDict = {}

        for i in s:
            sDict[i] = sDict.get(i, 0) + 1
        for i in t:
            tDict[i] = tDict.get(i, 0) + 1

        return sDict == tDict

        # time: O(n), space: O(n)
