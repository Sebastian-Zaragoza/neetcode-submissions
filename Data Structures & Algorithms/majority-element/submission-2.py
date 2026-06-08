"""
Elements
nums - integer array
n - size of the array

Tasks
Return the majority element

Observations
What is the majority element?
It's the element that appears more than n/2 times in the array
Always exists in the array

In summary
Return the element that appears more than n/2 times in the array

[5,5,5,2,1,1,1]
[1,1,1,1,2,5,5,5]
n - 4

1 - majority element
candidate - actual element
counter - 0

Observations
How would I use the elements found?
I will use the nums to iterate through all elements, I will take each element as possibles
candidates until to find the best one using the condition of n//2 

What if?
What if the array is empty?
Return 0

What would happen if?
What would happen if the algorithm doesn't find another candidate than the first one?
Return this, because the documentation specifies that always this exists

How would I solve this intuitively?
1. Check if the array is empty. If it's, return 0
    1.1 Sort the array
2. Initialize the majority_element and candidate variables
3. Initialize the general counter
4. Compute the threshold - n//2
5. Iterate through all elements in the array
6. Check in each iteration if the counter is greather than the threshold computed and the 
index is equal than the position of the last element
7. If it's true, change the majority element using the candidate found
8. Otherwise, cahnge the candidate by the actual element found and reset the counter to 0
9. Return the majority element found

What time complexity be?
O(n)

What space complexity be?
(1)
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums = sorted(nums)
        majority_element = nums[0]
        candidate = majority_element
        counter = 0
        threshold = len(nums)//2
        for i in range(len(nums)):
            if nums[i] != candidate or i == len(nums)-1:
                if counter >= threshold:
                    majority_element = candidate
                candidate = nums[i]
                counter = 0
            counter+=1
        return majority_element
            


