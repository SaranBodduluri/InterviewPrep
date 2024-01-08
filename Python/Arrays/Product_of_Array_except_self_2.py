from collections import Counter
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 1. Approach of using left and right arrays
        # left has the prefix product , right has the suffix product, ans = left* right for that element
        # two traversals
        # can be done in one traversal too!
        # first traversal with 0 index as 1 , calc. left suffix product
        # then in the same arrray traverse from right and calc. right suffix product
        # this is O(N) time complexity , O(1) space complexity

        ans = [0]*len(nums)
                
        # answer[i] contains the product of all the elements to the left
        # for the element at index '0', there are no elements to the left,
        # so the answer[0] would be 1
        ans[0] = 1
        for i in range(1, len(nums)):
            ans[i] = ans[i-1]*nums[i-1]
            # answer[i - 1] already contains the product of elements to the left of 'i - 1'
            # Simply multiplying it with nums[i - 1] would give the product of all 
            # elements to the left of index 'i'

        # R contains the product of all elements to the right
        R = 1
        # lets use REVERSED
        for i in reversed(range(len(nums))):
            ans[i]= ans[i]*R
            R*=nums[i]
        return ans
