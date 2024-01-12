class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # maintaining a char set approach 
        # along with two pointers

        start = 0
        ans = 0
        char_set = {        }

        for i in range(len(s)):
            if s[i] in char_set and char_set[s[i]] >=start:
                # already unte problem kadu
                # already undi, current window lo undi ante 
                # appudu window update cheyyali
                start = char_set[s[i]]+1
            char_set[s[i]] = i
            ans = max(ans, i - start+1)
        return ans
