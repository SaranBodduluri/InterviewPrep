class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start= 0
        current = ""
        ans = 0
        for end in range(len(s)):
            if s[end] not in current:
                current += s[end]
                ans = max(ans, len(current))

            else:
                current = current[current.index(s[end])+1:] + s[end]

                ## current lo last time s[end] tarvatha nunchi + ippudu malla chusam kabatti last lo add cheyali
        return ans              
