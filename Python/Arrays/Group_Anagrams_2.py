
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for i in strs:
            sorted_word = str(sorted(i))            
            # since the sorted word for a pair of anagrams is same
            # we are going to use it as the Key, with Values in the dict as anagrams list
            anagrams[sorted_word].append(i)
        return list(anagrams.values())

# DefaultDict
# The defaultdict is a dictionary of Python, which is like a container present inside the 'collections' module. 
# It is a sub-class of the dictionary class which is used for returning the dictionary-like object. 
#Both defaultdict and dictionary have the same functionality, except defaultdict never raise any KeyError as it provides a default value for the Key, which does not exist in the dictionary created by the user.

# syntax
# defaultdict(default_factory)  
#  The default_factory() function returns the **default value set** by the user for the dictionary defined by them. If this argument is absent, then the dictionary will raise the KeyError(it will become a normal dict).


# We can use a "List" as a default_factory
# creates a defaultdict with the *values that are set in list format.*
