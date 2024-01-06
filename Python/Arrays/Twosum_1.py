
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            a = nums[i]
            if int(target - a) in nums[i+1:]:
                return i,nums.index(target-a, i+1) 


# List index() Method Syntax
# list_name.index(element, start, end)
