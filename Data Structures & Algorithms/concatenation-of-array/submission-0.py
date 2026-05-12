"""
Elements:
nums - integer array
n - length of the nums array

Task: 
Create an return array

What should be the name of array?
The name of the array should be ans

Wha should be the length of the array?
2n

What is the condition to store elements within the array?
ans[i] == nums[i]
ans[i+n] == nums[i]

What is the condition for i?
0 <= i < n

In summary: Create an array that will contain duplicated elements of nums array

--Think about how to use the elements involved here?--
[1,4,1,2]
ans = [0]*(2*n)
ans[i] = nums[i]
ans[i+n] == nums[i]

--Unexpected cases--
What if?
What would happen if?

[] - []
[1,1] - [1,1,1,1]
[-1] - [-1,-1]


How would I solve this intuitively?
1. Check if the array - nums is empty. It true, return another empty
2. Use the legnth of the array - n for creating another array within 0's based on the sintaxis declared
3. Iterate trhough all elements in the array - nums
4. While the algorithm iterates, put all of the occurrences in the new array
5. At the end, return the new array created - ans

What would the answer be?
A new array called ans with 2n length

What should the time complexity be?
O(n)

What should the space complexity be?
O(2n)

What resources do you need?
Arrays, for loop, pointer, conditionals
"""

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 0:
            return []
        ans = [0] * (2*n)
        for i in range(0, n):
            ans[i] = nums[i]
            ans[i+n] = nums[i]
        return ans


    