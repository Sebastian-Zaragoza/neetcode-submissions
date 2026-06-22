"""
Elements
numbers - array of integers

Tasks
Return the indices (1-indexed) of two numbers, such that they add up to a given target number

Observations
The array is sorted in non-decreasing order
index1 < index2
index1 != index2 -> The are not the same index
Your solution must use O(1) additional space

In Summary
Return the indices in 1-indexed format of the two elements that add up to to a given target number

How would I use the elements found?
I would use the array to iterate through the elements and the target number to know what is the
remaining that I'm looking for

What if the array is empty
Return an empty array

What if does the array have duplicates?
It doesn't matter because every element is evaluated and taken as remainders. It the pair
is here, I would use it

How would I solve this intuitively?
1. Check if the array is empty. If it's return an empty array
2. Initialize an hashmap to register all of the elements evaluated
3. Iterate through all elements in the array
4. Take the element pointed and compute the difference between this and the target element
5. Search this difference in the hashmap.
6. If it's not, add the element on the hashmap
7. If there is a duplicated, update the poistion saved to the new one
8. If it's, take the poistion saved as the index1 and the poisition of the element pointed
as the index2. Increase 1 value for each of them and return the array of this pair
"""
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if len(numbers) == 0:
            return []
        hashmap = {}
        for i in range(0, len(numbers)):
            difference = target - numbers[i]
            if difference in hashmap:
                return [hashmap[difference]+1, i+1]
            hashmap[numbers[i]] = i
            
        