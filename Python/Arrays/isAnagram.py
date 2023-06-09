

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    
        if ((str(sorted(s))== str(sorted(t))) and len(s)==len(t)):
            return True
        else:
            return False


## sorted and same length
## The & operator is a bitwise AND operator, not a logical AND operator. When used with boolean values, the & operator performs a bitwise operation on the binary representations of the values, which is not the intended behavior in this case.

##### To fix the issue, you should use the logical AND operator and instead of the bitwise AND operator &.
    # SORT AND LENGTH. F YA
    #AttributeError: 'str' object has no attribute 'sort'
    # .sort is bs, 
    ## use sorted(string) 
    ## NOT LENGHTSof sets
    ## NOT sets ('a' and 'aa' )
    # NOT SETS AND LENGTHS of OGS, 
