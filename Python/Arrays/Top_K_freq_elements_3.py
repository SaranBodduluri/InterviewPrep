from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # only top k frequent elements
        # using Min heap, instead of sorting
        # ref: https://leetcode.com/problems/top-k-frequent-elements/editorial/

        # Complete Binary Tree
        # The Value of each node is less than or equal to the value of its children.

        # add acc. to the min heap conditions, pruning becase we only need Top K, so K nodes
        # are enough. 
        # so after K nodes are inserted every nodes that comes in, will go through re arranging and the tree will go through parsing

        # O(nlogK)


        # 1. Way to Count objects in dictionary
        # word= 'something'
        # counter = {}
        # for letter in word:
            # counter[letter] = counter.get(letter,0)+1
        # dict.get with 0 as a default value.
        

        # 2. using default dict
        # counter  = defaultdict(int)
        # for letter in word: counter[letter]+=1
        # Counter is a subclass of dict that’s specially designed for counting hashable objects in Python. It’s a dictionary that stores objects as keys and counts as values. 

        
        # 3. Using counter
        # from collections import Counter
        # Counter (some list or string)
        # Once you have a Counter instance in place, you can use .update() to update it with new objects and counts. 
        # most_common()
        #If you supply an integer number n as an argument to .most_common(), then you get the n most common objects.

        # import heapq
        # each time the smallest heap element is popped(min-heap). Whenever elements are pushed or popped, heap structure is maintained.

        # heapq.heapify(some list)
        # heapq.heappush(heap name, element)
        # heqpq.heappop(heap name) # removes the smallest element from the heap, order adjusted
        # heapq.heappushpop(heap, ele) # combines pushing and popping in one statement
        # heapq.heapreplace(heap, ele)

        # heapq.nlargest(k, iterable, key = fun.) returns the k largest elements from the iterable specified and satisfy the key is mentioned.
        # heapq.nsmallest(k, iterable, key = fn.) returns the k smallest elements from the iterable specified and satisfy the key if mentioned

        # dictionary . get() method
        # dictionary.get(keyname, value)
        # keyname of the item you want to return the value from
        # a value to return if the specified key does not exist. 

        # soln.
        if k == len(nums):
            return nums # O(1) time

        count = Counter(nums) 
        # building hashmap: num and hom many times it appears O(N) time
        return heapq.nlargest(k, count.keys(), key = lambda x: count[x])
        # the key parameter needs to be a function
        # so give me the nlargest keys sorted based on count(of the key)




