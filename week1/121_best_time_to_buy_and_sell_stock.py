class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        #intuition: we keep calculating max with prices lower than our current LOWEST price. if we find a new price lower than our lowest price, than we update lower price to gurantee max profit

        maxProfit = 0
        lowest = prices[0]

        for i, p in enumerate(prices):
            if i == 0:
                pass

            maxProfit = max(maxProfit, p - lowest)
            if p < lowest:
                lowest = p

        return maxProfit

        #time: O(n), space: O(1)
