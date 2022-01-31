class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        current_index = 1
        n = len(nums)
        
        for i in range(1, n):    
            if nums[i] != nums[i-1]:
                nums[current_index] = nums[i]
                current_index += 1
                
        return current_index