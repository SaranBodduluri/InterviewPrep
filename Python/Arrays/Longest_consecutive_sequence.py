class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # set and "in" checks approach
        # no sorting.
        if not nums:
            return 0

        longest_streak = 0
        num_set = set(nums)
        for num in num_set:
            if num - 1 not in nums: ## so that is the first # in the sequnce
                current_num = num
                current_streak = 1
                while current_num + 1 in nums:
                    current_num+=1
                    current_streak+=1
            
                longest_streak = max(longest_streak, current_streak)  # update longest streak after each while loop

        return longest_streak
