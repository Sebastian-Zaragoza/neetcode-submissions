
"""
Elements
array - s

Tasks
Write a solution to reverse the string

Considerations
Modify the input array, achieving a O(1) space complexity

In summary: Reverse the elements within the input array and not return 

['e'] = 1
['n', 'e'] = 2 
['e', 'm', 'n'] = 2

Observations
How to use the elements found?
I would use the array called s to reverse its elements 

What if?
What if the array is empty?
I would do nothing

What if does the array contain one element?
I would do nothing

What if does the array contain duplicate elements?
I would do nothing because it doesnt matter if the array contains repetitive elements. I doesnt affect 
the algorithm's performance and the final solution

What would happen if do the pointers point to the same element?
I would stop the evaluation

How would I solve this intuitively?
1. Check if the array contains zero or one element. If true, break the process and do nothing
2. Initialize two pointers
3. One pointer should point at the start and the another at the end
4. Repetive the next process until the two pointers point to the same element
5. Initialize a container to store the element will be added
6. Change the position of the elements pointed and use the container created
7. Update the pointers position

What would the time complexity be?
O(n)

Wha would the space complexity be?
O(1)
"""

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        start, end = 0, len(s)-1
        while start < end and end <= len(s)-1:
            end_element = s[end]
            s[end] = s[start]
            s[start] = end_element
            start+=1
            end-=1
        



        