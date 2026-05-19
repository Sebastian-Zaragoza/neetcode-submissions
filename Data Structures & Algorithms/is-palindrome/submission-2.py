"""
Elements:
string - s

Tasks:
Return true if the string is a palindrome, otherwise return false

Considerations:
Palindrome is a string that reads the same forward and backward, ignoring all non-alphanumeric characters
Alphanumeric characters - A,Z,a,z,0,9

In summary: Return a boolean value depending if the string is a palindrome or not, evaluating
alphanumeric characters

Observations
How to use the elements found?
I use the string s as the string that I evaluate
I evaluate the elements within it 

What if?
What if the array is empty?
Return true

What if does the array contain special characters?
Evaluate them if they are an alphanumeric character

What would happen if the start pointer is greather than the another one?
The evaluation process would end 

How would I solve this intuitively?
1. Check if the string is empty. If true, return tru
2. Initialize two pointers - start and end
3. Iterate through all elements in the string
4. Check if the start pointer is less than the end pointer and if the actual value pointed 
is an alphanumeric character
5. Apply the same logic for the end pointer
6. Compare if the elements pointed are the same. If false, return false
7. After evaluate all elements of the string, return true

What would the time complexity be?
O(n)

What would the space complexity be?
O(1)
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        start, end = 0, len(s)-1
        while start < end:
            while start < end and not s[start].isalnum():
                start+=1
            while end > start and not s[end].isalnum():
                end-=1
            if s[start].lower() != s[end].lower():
                return False
            start+=1
            end-=1
        return True

        
        