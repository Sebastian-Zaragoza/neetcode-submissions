class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        reader = 0
        for writter in range(1, len(nums)):
            if nums[writter] != nums[reader]:
               reader+=1
               nums[reader] = nums[writter]
        return reader+1
