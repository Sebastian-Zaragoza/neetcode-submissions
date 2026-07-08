"""
Elements
integer array - heights

Tasks
Return the maximmum amount of water a container can store

Observations
heights[i] - represents the height of the ith bar
you may choose any two bars to form a container

In Summary
Find the container that have the maximum amount of water using any two bars within the array

Base * Height
Base - difference between the bars choosen
Height - the minimum value between the two bars choosen

max_container = 36

[1,7,2,5,4,7,3,6]

How would I use the elements found?
I would use the array to evaluate evey element within it
I would use pointers to fin the container that has the maximum ammount of water

What if the array is empty?
I would return 0

What if the array has one element?
I would return the same element

What would happen if the the container found is not the best option?
Check what is the pointer that points to the minimum value and update this depending of its purpose

What would happen if the pointers point to the same value in different positions?
Move the start pointer forward instead of moving both of them

What would happe if the pointers point to the same element in the same position?
Finish the algorithm

How would I solve this intuitively as a brute force solution?
1. Check if the array is empty. If it's, return 0
2. Check if the array has a single value. If it's, return 0
3. Initialize two pointers, the first one in the start of the array and the another in the end of the array
4. Compute the area using the minimum value found
5. If it's greather than the maximum value registered, change it
6. Update the pointer that points to the minimum value found and continue
7. If both of the pointers point to the same element in different positions, move the start pointer
8. If both of the pointer point to the same eleent in the same position, finish the evaluation
9. Return the maximum value found
"""
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if len(heights) == 0 or len(heights) == 1:
            return 0
        start, end = 0, len(heights)-1
        maximum_container_area = 0
        while start < end and end <= len(heights)-1:
            minimum_value = min(heights[start], heights[end])
            maximum_container_area = max(maximum_container_area, (end - start)*minimum_value)
            if heights[start] == minimum_value or (heights[start] == minimum_value and heights[end] == minimum_value):
                start+=1
            else:
                end-=1
        return maximum_container_area
            
        