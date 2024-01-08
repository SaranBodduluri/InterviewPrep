from collections import Counter

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ## Skip duplicates!
        ## use Sorting!
        # three pointer approach, i , left, right
        nums.sort()
        ans = []
        # till len(nums)-2 to ensure that there at least 2 items after i
        for i in range(len(nums)-2):
            if i>0 and nums[i]== nums[i-1]:
                continue # skip, move to next i
            left, right = i+1, len(nums)-1
            while left < right:
                total = nums[i] + nums[left]+ nums[right]
                if total<0:
                    left+=1
                elif total>0:
                    right-=1
                else:
                    # if nums[i]!= nums[left] != nums[right]:
                    ## this DOES NOT WORK
                    ## it checks left to right
                   ##  it first checks if nums[i] is not equal to nums[left]
                    #   then it checks if nums[left] is not equal to nums[right]. However, it   doesn't guarantee that all three values are distinct.
                    
                    
                    ans.append([nums[left], nums[i], nums[right]])
                    left +=1
                    right -=1
                    while left < right and nums[left] == nums[left-1]:
                        left+=1
                    while left< right and nums[right] == nums[right+1]:
                        right-=1

        ## lets filter duplicates separately
        seen = set()
        unique_ans = []
        for thing in ans:
            sorted_thing = tuple(sorted(thing))
            if sorted_thing not in seen:
                seen.add(sorted_thing)
                unique_ans.append(list(sorted_thing))
            # tuple(sorted) because tuple is hashable and 
        # list is non-hashable type and hence cant be used for " not in"  step

        # , lists are mutable objects, so they are unhashable and cannot be
        # directly used as keys in a set or dictionary. 

        return unique_ans
