"""
Elements
Enconded string
Decoded string

Tasks
To encode a list of strings to a string

Observations
The encoded string is then sent over the network and is decoded back to the original list of string

In Summary
Design two algorithms to encode and decode strings

Free Space
["Hello", "World"]
5#Hello5#World

How would I use the elements found?
I would use the list of strings to merge them into a single one and add the correct delimiters
to separate the words and generate the same list of words again

What if the list of string is empty?
Return nothing

What if the string expected is empty?
Return an empty list

What would happen if the list of string have some words with uppercase letter and numbers?
It doesn't matter because I add as a introductory delimiter the size of the words - I mean, the
total of characters related to the next word and a separator to differentiate these

How would I solve this intuitively?
1. Initialize an empty string
2. Iterate through all elements of the list
3. Before to add the word in the empty string, add the number of characters involved and the delimiter assigned - ##
4. Repeat the proccess for all of them
5. Initialize an empty array
6. Initialize a pointer with 0
7. Extract the number that is related to the total of characters involved and add 1 to the new pointer
8. Initialize another loop to extract all of the characters using the size of the word extracted
9. Update the pointer adding 1 
10. Repeat the process for the rest of the string
11. Return the list of strings decoded
"""
class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for w in strs:
            s += str(len(w)) + '#' + w
        return s

    def decode(self, s: str) -> List[str]:
        list_strings = []
        pointer = 0
        while pointer < len(s):
            subpointer = pointer
            while s[subpointer] != '#':
                subpointer+=1
            length = int(s[pointer:subpointer])
            list_strings.append(str(s[subpointer + 1: subpointer + 1 + length]))
            pointer = subpointer + 1 + length
        return list_strings
        