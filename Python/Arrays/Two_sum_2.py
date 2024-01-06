class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        # using a map increases the space complexity to n 
        # and makes the time complexity n
        for i in range(len(nums)):
            complement= target - nums[i]
            if complement in hmap:
                return [i, hmap[complement]]
            else:
                hmap[nums[i]] = i
        return [] # no soln

## key value pair in the map should be number itself and index
# be careful b/w i and nums[i]

# you can use enumerate as well
