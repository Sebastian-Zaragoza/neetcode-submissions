"""
Elements
nums1, nums2 - integer arrays
m - is the number of valid elements in nums1
n - is the number of elements in nums2

Tasks
Merge the two arrays in nums1 sorted in non-decreasing order
Not return anything

Observations
Both arrays are sorted in non-decreasing order
nums1 has a total of length (M+N)
The first M elements are the values to be merged
The N elements set to 0 as placeholders

In Summary
Merge all of the values in nums1 following the observations recomended and not return anything


[1,2,10,20,20,40] 
[1,2]

m = 4
n = 2


Observations
How would I use the elements found?
I would use (m+n) for initialize a pointer to add values in nums1, m for the nums1 pointer and
n for the nums2 pointer

What if?
WHat if the arrays are empty?
Do nothing

What if the nums1 array is empty?
Continue with nums2

What would happen if?
What would happen if the nums1 pointer is out of the index?
Automatically add the remaining elements in nums2. The same logic applies when nusm2 pointer is out
of the index

How would I solve this intuitively?
1. Initialize the 3 pointers - adding, nums1, nums -- using the m and n variables
2. Iterate through the elements in nums1 and nums2 where nums1 and nums2 pointers are greather than 0
3. Check if the element pointed in nums2 is less than the element pointed in nums1, add the nums1 element
using the adding pointer
4. Otherwise, add the nums2 element adn decrease the pointer values
5. Continue until one of the pointers is out of index
6. If it's true, add the reamining elements of nums1 and nums2 respectivelly if there are

What time complexity be?
O(m+n)

What space complexity be?
O(1)
"""
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        adding_pointer = (m+n)-1
        nums1_pointer = m-1
        nums2_pointer = n-1

        while nums1_pointer >= 0 and nums2_pointer >= 0:
            if nums2[nums2_pointer] < nums1[nums1_pointer]:
                nums1[adding_pointer] = nums1[nums1_pointer]
                nums1_pointer-=1
            elif nums2[nums2_pointer] >= nums1[nums1_pointer]:
                nums1[adding_pointer] = nums2[nums2_pointer]
                nums2_pointer-=1
            adding_pointer-=1
        
        while nums1_pointer >= 0:
            nums1[adding_pointer] = nums1[nums1_pointer]
            nums1_pointer-=1
            adding_pointer-=1

        while nums2_pointer >= 0:
            nums1[adding_pointer] = nums2[nums2_pointer]
            nums2_pointer-=1
            adding_pointer-=1


        
        