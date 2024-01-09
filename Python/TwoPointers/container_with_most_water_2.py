class Solution:
    def maxArea(self, height: List[int]) -> int:
        #two pointer approach
        # explanation down

        # At every step, we find out the area formed between them, update
        # maxarea, and *move the pointer pointing to the shorter line* 
        # **towards the other end** by one step.
        i, j = 0, len(height)-1
        maxarea = 0
        while i<j:
            maxarea = max(maxarea,min(height[i], height[j])*(abs(i-j)))
            if height[i]<=height[j]:
                i+=1
            else:
                j-=1
        return maxarea
        
            

# explanation:
#             [4 (left) , 9, 12, 7 , 8, 14 (right) ] --------> this array is indexed from 1 to 6 and we looks at left and right and compare the value

# So eliminate all pairs of index [1,2], [1,3],[1,4],[1,5] <- here the index[] means possible windows of solutions (4,9), (4,9,12), (4,9,12,7)...
# Why? area of window [1,6] = (6 - 1) * MIN(4, 14) = 20
# all the windows that have [1,2...5] even if all the numbers on the right are changed to infinity must be less than 20.
# EX:
# (5-1) * min(4, infinity) < 20 for all right indicies less than 6.
# So this means its ok to exclude all windows starting with index 1

# If you apply this at each step over and over again you can get an O(n) algorithm.
