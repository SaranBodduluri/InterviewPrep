class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # one pass approach
        # LOOK backward
        # the optimal buy point for a sell day is the lowest so far
        # so keep track of lowest and hight diff. ur done in single pass.

        # minprice and maxprofit corresponding to the smallest valley and maximum profit (maximum difference between selling price and minprice) obtained so far respectively.
        low = prices[0]
        maxp = 0
        for i in range(1,len(prices)):
            if maxp < prices[i] - low:
                maxp = prices[i] - low 
            if prices[i] < low:
                low = prices[i]
        return maxp


        # two loops ; doesnt work!!
        # maxp = 0
        # for i in range(len(prices)):
        #     now = prices[i]
        #     j = i+1
        #     while j<len(prices):
        #         if prices[j] > prices[i]:
        #             diff = prices[j]- prices[i]
        #             maxp = max(diff,maxp)
        #         j = j+1
        # return maxp
