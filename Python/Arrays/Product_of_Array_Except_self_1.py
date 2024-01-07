from collections import Counter
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # multiply all numbers
        # divide by self, return
        # if 0, replace with 1 
        # calc. product. put the product where 0 is and put 0s everywehere else
        # another case more than 1 zero
        
        count = Counter(nums)
        if count.get(0,0) >1:
            return [0]*len(nums)
        if 0 in nums:
            # for the case of ONLY 0s in the array
            if list(set(nums))[0] ==0 and len(set(nums)) ==1:
                return nums 
            totpro=1
            for i in nums:
                if i !=0:
                    totpro*=i
            for i in range(len(nums)):
                if nums[i] ==0:
                    nums[i] = totpro
                else:
                    nums[i] =0
            return nums            

        totpro=1
        for i in nums:
            totpro*=i
        for i in range(len(nums)):
            nums[i] = int(totpro/nums[i])
        return nums
