"""
Elements:
array - nums

Tasks:
Return true if any value appears more tahn once in the array
Return false if there are unique values

Considerations:
Would I need to return the array?
No, just return a boolean value

What is the condition for any value in the array?
If appear_value > 1 - return true
Otherwise - return false

In summary: Return a boolean value depending of the condition.

Observations:
How to use the elements found?
nums- use this to iterate through the array, element by element
set - use this to store unique elements and facilitate getting values

What if?: - elements
What if there are negative values in the array?
The process would be the same, because it doesn't affect the algorithm's performance

What would happen if? - events
What would happen if there are more than once repetitive value in the array?
The algoritm would break the process and return a false boolean value

How to solve this intuitively?
1. Check if the array is empty. If true, return true
2. Initialize a set data structure
3. Iterate through all ellements in the nums array
4. Check if the element pointed is in the set, return false
5. Otherwise, continue
6. Afer evaluate all elements in the array, return true

What would the time complexity be?
O(n)

What would the space complexity be?
O(n)

"""

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False 
        set_elements = set()
        for i in range(0, len(nums)):
            if nums[i] in set_elements:
                return True
            set_elements.add(nums[i])
        return False


