"""
Elements
s - stringg

Tasks
Return the length of the longest substring without duplicate characters

Observations
Substring is a contiguous sequence of characters within a string

In Summary
Return the length of the longest substring without duplicate characters

Observations
How would I use the elements found?
I would use the string to itrerate through all elements within it. 
Additionally, I would use two pointers to group all posible susbtrings

What if the string is empty?
The result would be 0

What would happen if the pointer is out of the index?
The process would be broken and then, it would return the result

How would I solve this intuitively?
1. Initialize the container where the length of the longest substring would be stored, starting with 0
    1.1 Initialize a set to store all unique values 
2. Generate the start pointer with 0
3. Iterate through all elements in the string using another pointer
4. Check if the actual element pointed is in the set
    4.1. If it's false, add this 
    4.2 Otherwise, compute the difference between the end and start pointer and update the variable if the result is greather than the actual one
    4.3. After that, remove the element pointed by the start pointer and update this adding 1 until remove
    the element pointed by the end pointer
    4.4. Finally, add the value pointed by the end pointer
5. Return the length of the longest substring

What time complexity should be?
O(n)

What space complexity should be?
O(m)
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length_sub = 0
        set_values = set()
        start = 0
        for end in range(0, len(s)):
            if s[end] not in set_values:
                set_values.add(s[end])
                length_sub = max(length_sub, end+1 - start)
                continue
            while s[end] in set_values:
                set_values.discard(s[start])
                start+=1
            set_values.add(s[end])
        return length_sub




