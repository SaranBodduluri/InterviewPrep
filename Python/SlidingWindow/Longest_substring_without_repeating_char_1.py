class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # start = 0
        # ans = 0
        # ansstring = ""
        # precurrentwo = "" 
        # for end in range(1,len(s)):
        #     precurrentwo = s[start:end] # does not include end, only UNTIL end
        #     if s[end] in precurrentwo: 
        #         start = start+1### start + kadu, move to the last time s[end] +1  
        #     else:
        #         ans = max(ans, len(precurrentwo)+1)
        # return ans

        start = 0
        ans = 0
        current = ""

        for end in range(len(s)):
            while s[end] in current:
                current = current[1:]  # Remove the first character from the current substring, keep advacning 
                start += 1

            current += s[end]
            ans = max(ans, len(current))

        return ans
 
