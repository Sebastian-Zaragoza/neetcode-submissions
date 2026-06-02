"""
Elements
nums- array of integers
target - int

Tasks
Return the indices i and j AS AN ARRAY
Return the answer with the smaller index first

Observations
nums[i] + numms[j] == target
i != j

*Every input has exactly one pair of indices i and j that satisfy the condition

In Summary
Return an array with the indices of the elements which sum is equal than the target
Remember - There is only one solution

Observations
How would I use the elements found?
I would the array to iterate through all elements and evaluate them, also the target value
would be useful to check if the sum of the pair found is equal than this.

What if the array is empty or does it contain one value?
It's not possible due to the problem argues that there is only one pair that satisfies the problem

What if the array contain duplicates?
It doesn't matter, because I would consider the first occurrence 

What would happen if there are negative values?
I would sum them correctively respecting the negative signals

How would I solve this intuitively?
1. Initialize a container to register all values evaluated
2. Iterate through all elements in the array
3. While checking the actual value, compute the difference between the target value and the pointed one
4. If the difference is in the container, return their indices
5. Otherwise, add the value and its index in the container and continue
6. Before add the indices in the container to return, sort them
    6.1. For sorting, compare if the i index is greater than the another
    6.2. If it's true, add first the i index and then the j index, otherwise, swap them
7. Return the array that contains the indices of the values 
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(0, len(nums)):
            difference = target - (nums[i])
            if difference in hashmap:
                return [hashmap[difference], i]
            else:
                hashmap[nums[i]] = i




