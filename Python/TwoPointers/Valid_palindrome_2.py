class Solution:
    def isPalindrome(self, s: str) -> bool:
        # two pointer approach
            # Algo
    #         Set two pointers, one at each end of the input string
    # If the input is palindromic, both the pointers should point to equivalent characters, at all times. 1
    # If this condition is not met at any point of time, we break and return early. 2
    # We can simply ignore non-alphanumeric characters by continuing to traverse further.
    # Continue traversing inwards until the pointers meet in the middle.

        i, j = 0, len(s) -1
        # ignore not isalnum
        while i < j:
            while i<j and not s[i].isalnum():
                i+=1
            while i<j and not s[j].isalnum():
                j-=1
            if s[i].lower() != s[j].lower()
                return False
            i+=1
            j-=1
        return True

            
