from collections import Counter
import random
# Hoares Algo:
# Quickselect is a textbook algorithm typically used to solve the problems "find kth something": kth smallest, kth largest, kth most frequent, kth less frequent,
# Build a hash map element -> its frequency and convert its keys into the array unique of unique elements. Note that elements are unique, but their frequencies are not. That means we need a partition algorithm that works fine with duplicates.

# Work with unique array.
# Use a partition scheme (please check the next section) to place the pivot into its perfect position pivot_index in the sorted array, move less frequent elements to the left of the pivot, and more frequent or of the same frequency - to the right.

# Compare pivot_index and N - k.

# If pivot_index == N - k, the pivot is N - kth most frequent element, and all elements on the right are more frequent or of the same frequency. Return these top kkk frequent elements.

# Otherwise, choose the side of the array to proceed recursively (random pivot, partition)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = Counter(nums)
        unique = list(count.keys())

        # doing Lomuto's Partition
        # ref: https://leetcode.com/problems/top-k-frequent-elements/editorial/

        def partition(left, right, pivot_index):
            pivot_frequency = count[unique[pivot_index]]
            # move the pivot to the end
            unique[pivot_index], unique[right] = unique[right], unique[pivot_index]

            # move all less frequent elements to the left
            # all the same or more frequent elements will go to the right
            store_index = left # store index starts at left
            for i in range(left, right):
                if count[unique[i]]< pivot_frequency:
                    unique[store_index], unique[i] = unique[i], unique[store_index]
                    store_index+=1
            
            # move the pivot to the final place
            unique[right], unique[store_index] = unique[store_index], unique[right]

            return store_index
            # Store index was the where the pivot was finally after the partition

        def quickselect(left, right, k_smallest) -> None:
            """
            sort a list within left .. and .. right till kth less frequent element takes its place
            """

            # base case: the list has only one element
            if left == right:
                return

            # select a random pivot_index b/w left and right
            pivot_index = random.randint(left, right)
            # find the pivot position after the sorting
            pivot_index = partition(left, right, pivot_index)

            # if the pivot is in its final sorted position
            if k_smallest == pivot_index:
                return
            # go left, we can ignore the right side
            elif k_smallest < pivot_index:
                quickselect(left, pivot_index - 1, k_smallest)
            # go right
            else:
                quickselect(pivot_index + 1, right, k_smallest)

         
        n = len(unique) 
        # Kth top frequent element is (n-k)th less frequent
        # do a partial sort: from less frequent to the most freq, till (n-k)th less frequent element takes
        # place (n-k) in a sorted array.
        # all elements on left are less frequent
        # all elements on right are more frequent   
        quickselect(0, n-1, n-k)
        # Return top k frequent elements
        return unique[n-k:]

        # O(N) time complexity, using master theorem...
        # : T(N)=T(N/2)+N , case with random pivots
 
