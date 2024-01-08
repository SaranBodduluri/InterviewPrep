class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums: # nothing case
            return 0
        sortnum = sorted(set(nums))
        ## removing duplicates is NECESSARY, coz might lead to unnecessary zeroing of count....
        count = 1
        max_count =  1
        for i in range(1, len(sortnum)):
            diff = sortnum[i] - sortnum[i-1]
            if diff == 1:
                count+=1
            else:
                max_count = max(max_count, count)
                count = 1
        return max(max_count, count)
        # **in case the LONGEST sequence is at the end of the list, **
        # so return max of max_count and the count
