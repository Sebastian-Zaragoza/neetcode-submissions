"""
Elements
string - s
integer - k

Tasks
After performing AT MOST K replacements, return the length of the longest substring 
which contains only one distinct character

Observations
s - contains only uppercase english characters 
k - number of characters available to replace

In Summary
Return the length of the longest substring which contains only one distinct character and the rest 
as repetitive ones

-AAABABB-
k - 1
Check if the character is in the container
Evaluate what is the most frequent character
Compare if the actual character is equal than the most frequent

How would I use the elements found?
I would use the string to evaluate character by character and k to stablish a limit of replacements

What if the string is empty?
I return 0

What if the k value is equal than the length of the string?
I return the lenght of the string

What would happen if does the string contain duplicates?
I would take the most repetitive character as the most frequent to compare between the rest of the elements

How would I solve this intuitively?
1. Check if the string is empty. If it's return 0
2. Check if the k value is equal than the length of the string, if it's return the same 
3. Initiaize a hashmap to track the frequency of each character and the pointer for the window
4. Evaluate character by character
5. Check if the actual character is in the hasmap. If it's not, add this with a 1, otherwise, increment 1
6. Iterate through all elements in the hashmap and extract the most frequent
7. If the actual one is the same than the extracted, continue 
8. Otherwise, continue if the counter is less or equal than the k value
9. If the number of replacements is achieve, increment the start pointer and every time that
this points to a character different than the most frequent, reduce the counter and continue
10. Compute the longest susbtring every iteration and return it at the end of the process
"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = {}
        max_freq = 0
        longest_sub = 0
        start = 0

        for end in range(len(s)):
            hashmap[s[end]] = hashmap.get(s[end], 0) + 1
            max_freq = max(max_freq, hashmap[s[end]])
            while (end - start + 1) - max_freq > k:
                hashmap[s[start]] -= 1
                start += 1
            longest_sub = max(longest_sub, end - start + 1)
        return longest_sub
            



