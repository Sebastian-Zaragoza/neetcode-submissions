"""
Elements
nums - array
k - integer

Tasks
Return true if there are TWO DISTINCT INDICES - I,J NOT VALUES
WHERE the absolute value of i-j should be less or equal than k
OTHERWISE return false

Observations
nums[i] should be equal than nums[j]
abs(i-j) <= k


In summary - RETURN TRUE if there are two distinct indices with same values and the absolute result of them
should be less or equal than K, otherwise, RETURN FALSE

Observations
How to use the elements found?
I'll use the array to iterate through all elements 
I'll use the k value to evaluate the final result 

What if?
What if the array is empty?
Return False

What if the array contains a lot of duplicates?
I would take the first two ocurrences

What if the array doesn't contain duplicates?
Return False

What would happen if?
What would happen if the array doens't contain duplicates, contains one element or at least two distinct element?
Return False

What would time complexity be?
O(n)
What would space complexity be?
O(n)

How would I solve this intuitively?
1. Initialize two pointers - start and end
2. Iterate though all elements within the array
3. Evaluate using the end pointer the next element
4. If the pointer is not in the hashmap, add this and its index
5. Then, move forward the pointer
6. If the pointer finds an exact match within the array and in the hashmap, computes the abs value
7. If the value is less or equal than k, return True
8. If it's false, update the start point using the index store and change it for the new occurrence
9. At the end, return False
"""

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = {}
        for j in range(0, len(nums)):
            if nums[j] not in hashmap:
                hashmap[nums[j]] = j
            elif nums[j] in hashmap:
                i = hashmap[nums[j]] 
                abs_value = abs(i-j)
                if abs_value <= k:
                    return True
                else:
                    hashmap[nums[j]] = j
        return False
            
