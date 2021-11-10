class Solution(object):
    def moveZero(self,nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        index = 0
        i = 0
        for i in nums:
            if i != 0:
                nums[index] = i
                index += 1
                
        for z in range(index, len(nums)):
            num[z] = o
        

        

        
