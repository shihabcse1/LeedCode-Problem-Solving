class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        nums_len = len(nums)
        
        if nums_len == 0:
            return 0
            
        for i in range(nums_len):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
                
        return k