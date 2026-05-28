"""
Elements: 
strings - s,t

Tasks
return True if the two strings are anagrams of each other
otherwise, return False

Observations
An anagram is a string that contains the exact same characters as another string
but the order can be different

In summary - Evaluate if both of the strings are anagrams 

s = "racecar", t = "carrace"

How would I use the elements found?
I would use both of the strings, transforming them into patterns and at the end, evaluate these patterns

What if one string is different than the other one?
I return False

What if both strings are empty?
I return True

What would happen if the legnth of one string is different than the another?
I would evaluate each string separately 

How would I solve this intuitively?
1. Start to evaluate the string s, letter by letter
2. Generate a container to store the pattern of s letters with 0's
3. Compute the equivalence of the letter pointed using ord
    3.1 Why to use ord function?
        To compute the alphabetic-integer value
4. Use this equivalence as an index to add a value if there is a 0, otherwise, add 1
5. Repeat the process for the other string
6. Convert the arrays into strings and compare them
7. If these are the same, return True, otherwise, return False

What would time complexity be?
O(n+m)
What would space complexity be?
O(1)
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_container = [0]*27
        t_container = [0]*27
        for letter_s in s:
            equivalence_s = ord(letter_s) - ord('a')
            s_container[equivalence_s] +=1 
        for letter_t in t:
            equivalence_t = ord(letter_t) - ord('a')
            t_container[equivalence_t] +=1
        s_container = ''.join(str(s_letter) for s_letter in s_container)
        t_container = ''.join(str(t_letter) for t_letter in t_container)
        return s_container == t_container


        