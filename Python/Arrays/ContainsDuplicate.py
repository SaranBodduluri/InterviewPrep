class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        num2 = set(nums)
        if len(num2) !=len(nums):
            return True
        else:
            return False
        
        # num2 = []
        # for i in nums:
        #     if i not in num2:
        #         num2.append(i)
        # if len(num2) !=len(nums):
        #     return True
        # else:
        #     return False


        # num2 = []
        # for i in nums:
        #     if i in num2:
        #         return True # there is some duplicate!
        #     num2.append(i)
        # return False
