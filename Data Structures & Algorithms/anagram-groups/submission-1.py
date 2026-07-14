"""
Elements
array of strings - strs

Tasks
Group all anagrams together into sublists

Observations
You may return the output in any order
An anagram is a string that contains the exact same characters as another string

In Summary
Return an array of strings grouped by anagrams in any order
---------------------
["act","pots","tops"]
{} act - a c t
   tac - a c t
   posts - o p ss t
   tops - o p s t
---------------------

How would I use elements found?
I would take the strs array to iterate through all words and then, each letter one by one

What if the array is empty?
Return the same array

What would happen if I have a new word to evaluate?
I would compute the pattern that it follows

What would happen if the word evaluated does have letters duplicated?
I would increase the number of times that this letter appears

How would I concatenate all of the words based on their anagram pattern?
I would append them into arrays one by one depending on their anagram pattern

How would I solve this intuitively?
1. Check if the array is empty. If its, return the same array
2. Iterate through all elements in the array
3. For each element, initialize an empty array with 0's which it's size should be 26 (total of letter in the English vocabulary)
4. Iterate through all letters of the word and compute their equivalence, taking it as the index to add 1 value
5. Convert this equivalence into a string and save this in a hashmap addingg the word related
6. If the pattern has been found, just add the word related
7. Iterate through all elements in the hashmap and add them into a new array based on their anagram pattern
8. Return the final array
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return []
        hashmap = {}
        for word in strs:
            pattern_word = [0]*26
            for letter in word:
                pattern_word[ord(letter) - ord('a')] += 1
            pattern_anagram = ','.join(str(i) for i in pattern_word)
            if pattern_anagram not in hashmap:
                hashmap[pattern_anagram] = []
            hashmap[pattern_anagram].append(word)
        final_array = []
        for pattern, word_list in hashmap.items():
            final_array.append(word_list)
        return final_array


            

        
            

