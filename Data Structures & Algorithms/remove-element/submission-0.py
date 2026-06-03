class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        - Integer array - nums
        - Integer value - val
        *Remove all aocurrences of val from nums in-place
        *In place - Remove the ocurrences from the original array
        -Return the number of remaining elements - k
        - K represents all elements differtent than val
        *The first k elements of nums do not contain val
        *The order of the elements is not relevant
        *Not repeat any number which is not equal than val
        
        In Summay - Return k (elements which are not equal than val) without repetitions
        """
        """
        How to solve this intuitively?
        1. Check element by element from the array and compare these values
        2. If one of them is equal than val, remove this
        3. At the end, count all of the values in the array and return the length of this
        
        Assumptions
        What the answer should be?
        The answer should be k - unique elements different than val
        Would I need to replace elements from the original array?
        Yes, I would need to replace them
        Is the order important for the original array?
        No, the order is irrelevant

        Observations
        What kind of structures would I need to use?
        Arrays
        Would I need to use conditionals and loops?
        Yes, I need to implement a for loop to iterate through the array and conditional to know if the value
        is equal than val 
        """
        i = 0
        while i <= len(nums)-1:
            num = nums[i]
            if num == val:
                del nums[i]        
                continue
            i+=1              
        return len(nums) 

