"""
Elements
string - s1, s2

Tasks
Return true if s2 contains a permutation of s1
Return false otherwise

Observations
Both susbtrings only contain lowercase letters

In Summary
Return a true if s2 contains a permutation of s1, otherwise, return false


s1 - "abc"
[1110000000000000000000000]

s2 - "lecabe"
[1110000000000000000000000]

How would I use the elements found?
I would iterate through s2 and compare the context and length of s1

What if s1 is greather than s2?
Return false

What if s2 is empty?
Return false

What if s1 is empty?
Return true

What would happen if the difference between the pointers is equal than the length of s1?
Become to compare the pattern computed and if its not equal than the pattern of s1, add and delete
one element using start and end pointers

How would I solve this intuitively?
1. Check if s1 is greather than s2 and if s2 is not empty. If it's return false. 
2. Check if s1 is empty. If it's return true
3. Compute the pattern of the s1's context - array of 26 spaces -> string
4. Cover elements one by one until to get the length of s1 between the pointers
5. When it's achieve, compute the pattern found and compare with the s1 calculated. 
6. If they are the same, return true, otherwise, delete by start pointer and add one by end pointer
7. Return false if the end pointer is out of the index
"""
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2) or len(s2) == 0:
            return False
        if len(s1) == 0:
            return True
        pattern_s1 = [0]*26
        for c in s1:
            pattern_s1[ord(c) - ord('a')] += 1
        pattern_s1_s = ''.join(str(s) for s in pattern_s1)
        start, end = 0, 0
        pattern_s2 = [0]*26
        while end-start <= len(s1)-1:
            pattern_s2[ord(s2[end]) - ord('a')] +=1
            end+=1
        pattern_s2_s = ''.join(str(s) for s in pattern_s2)
        if pattern_s1_s == pattern_s2_s:
            return True
        while start <= end and end <= len(s2)-1:
            pattern_s2[ord(s2[start])-ord('a')] -=1
            pattern_s2_s = ''.join(str(s) for s in pattern_s2)
            if pattern_s1_s == pattern_s2_s:
                return True
            pattern_s2[ord(s2[end])-ord('a')] +=1
            pattern_s2_s = ''.join(str(s) for s in pattern_s2)
            if pattern_s1_s == pattern_s2_s:
                return True
            start+=1
            end+=1
        return False

            

        