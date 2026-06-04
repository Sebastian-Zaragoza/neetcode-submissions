"""
Elements
word1, word2 - strings

Tasks
Construct a new string
Merge them in alternating order

Observations
Starting with word1 and then from word2
If one string is longer than the other, append the remaining characters form the longer string to the end

In Summary
Return a new string where the word1 and word2 strings are merged. If there are remaining characters,
add them to the end of the new string

"ab" "bbc"
"a, b, b, b, c"

Observations
What if both of the string are empty?
I return an empty array

What if one of the strings are empty?
I return the other string completly

What would happen if the pointer is outside of the string?
I automatically add all of the remainin characters to the end of the new string generated

How would I solve this intutitively?
1. Initiaize the two pointers
    1.1 Initialize the new string as an empty one
2. Put both of them at the start of the strings respectivelly
3. Evalute word1
    3.1. Check if the pointer is less or equal than the string's size. 
    3.2. Take the character pointed and add to the end of the new string
    3.3. Move the pointer forward to the next element, incrementing it's value
4. Evaluate word2 as the same way as word1 evaluation
5. Check if the word1 pointer is outside of the word1 size and the word2 pointer is less or equal than the word2 size
    5.1. If it's true, add all of the reamining characters to the new string, incrementing word2 pointer
6. Chec if the word2 pointer is outside of the word2 size, repetat the process of word1 pointer
7. Return the new string

What would time complexity be?
O(n+m)

What would space complexity be?
O(n)
"""
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1_pointer, word2_pointer = 0,0
        new_string = ""
        while word1_pointer <= len(word1)-1 and word2_pointer <= len(word2)-1:
            new_string += word1[word1_pointer]
            new_string += word2[word2_pointer]
            word1_pointer += 1
            word2_pointer += 1

        while word1_pointer <= len(word1)-1:
            new_string += word1[word1_pointer]
            word1_pointer+=1
        while word2_pointer <= len(word2)-1:
            new_string += word2[word2_pointer]
            word2_pointer+=1
        return new_string
        
        




