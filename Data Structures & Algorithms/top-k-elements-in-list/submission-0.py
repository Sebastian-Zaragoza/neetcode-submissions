"""
Elements
array - nums
integer - k

Tasks
Return the k most frequent elements within the array
You may return the output in any order

Observations
The answer is only unique

Summary
Return the most k repetitive elements within the array in any order

[1,2,2,3,3,3] k = 2

{
1: 1
2: 2
3: 3
}

 1 2 3 4 5 6  
[[1],[2],[3],[],[],[]]

[3, 2] == k

How would I use the elements found?
I would use the array to iterate through all elements and k value to know when to stop and return the possible candidates

What if k value is empty?
Return an empty array

What if the array is empty?
Return the same array

What would happen if the array have duplicates?
It doesn't matter, I would return the same occurence of this value

How would I solve this intuitively?
1. Check if the array or the k value are empty. If any of these is empty, return an empty array
2. Initialize a container to store all of the occurences of each value and a new empty array using the length
of the input. Fill the new one with empty arrays.
3. Iterate through all elements and add each element in the container
4. After that, iterate through all elements in the hashmap and use the number of frequencies as the index
in the new array and the value as the value contained
5. Once the array is filled, generate a new array to store all of the possible candidates
6. When every element is added, compare the length of the new array against the k value
7. If the size of the new array is equal than the k value, return this
"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == 0 or len(nums) == 0:
            return []
        hashmap = {}
        new_array = [[] for i in range(len(nums)+1)]
        for n in nums:
            hashmap[n] = 1 + hashmap.get(n, 0)
        for i, v in hashmap.items():
            new_array[v].append(i)
        final_array = []
        for i in range(len(nums), 0, -1):
            for n in new_array[i]:
                final_array.append(n)
                if len(final_array) == k:
                    return final_array