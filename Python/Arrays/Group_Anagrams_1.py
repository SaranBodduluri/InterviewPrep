class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        op = []
        checked = set() # checked is a set 
        # if a set of anagrams are done, they will be in checked
        for i in strs:
            if i not in checked:
                temp = [i]
                checked.add(i)
            # for loop starts only if i is not checked
                for j in strs[strs.index(i)+1:]:
                    if sorted(j) == sorted(i) and len(i) == len(j):
                        temp.append(j)
                        checked.add(j)
                op.append(temp)
 
        return op

## this will cause a TLE. !!!
