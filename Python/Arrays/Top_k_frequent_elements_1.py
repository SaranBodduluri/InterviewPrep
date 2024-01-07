import numpy as np
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums2 = np.array(nums)
        values, counts = np.unique(nums2,return_counts = True)
        # using the numpy unqiue function and nums2 as an argumdent
        ans =[]
        values = values[np.argsort(counts)]
        # doing numpy argsort of the counts, it gives ascending
        values = values[::-1]
        # reversing it so that we have the descending order
        return values[:k]
        # returning the top K frequent elements
