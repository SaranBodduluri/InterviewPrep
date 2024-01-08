class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = list(s)
        # for i in s:
        #     if i.isalpha() and i.isnumeric():
        #         pass
        #     else:
        #         s.remove(i)

        ## Removing characters while iterating is bullshit. you cant do that.
        s = ''.join(i.lower() for i in s if i.isalnum())
        return s == s[::-1]

        # python string method isalnum
        # returns if all the characters are alphanumeric

        # join() another bful string method>>>
