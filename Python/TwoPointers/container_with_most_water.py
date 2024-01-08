class Solution:
    def maxArea(self, height: List[int]) -> int:
        # get the best and the second best approach.
      ### this code fails. but i couldnt figure out why
        maxh = 0
        ind = 0
        for i in range(len(height)):
            if height[i] >maxh:
                ind = i
                maxh = height[i]
        secondmaxh =0
        #### DEL method; fuckedup
        ### if you use the DEL method, the initial structure is screwed up
        # del height[i]
        ## just skip the tallest!!

        ind2 = 0
        for i, h in enumerate(height):
            if h> secondmaxh and i!= ind:
                ind2 = i
                secondmaxh = height[i]
        return min(maxh, secondmaxh)*abs(ind-ind2)
            ## minimum of both the heights

