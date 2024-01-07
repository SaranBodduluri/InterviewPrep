class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        checked = set()
        for i in nums:
            if i not in checked:
                hmap[i] = 1
                checked.add(i)
            else:
                hmap[i]+=1
        sortedhmap = {ke:v for ke,v in sorted(hmap.items(), key= lambda item: item[1])}
        ## 
        return list(sortedhmap.keys())[-k:]
        ## getting top K

# Both list.sort() and sorted() have a ***key parameter to specify a function*** (or other callable) to be called on each list element prior to making comparisons.

# The value of the key parameter should be a function (or other callable) that takes a single argument and returns a key to use for sorting purposes.
