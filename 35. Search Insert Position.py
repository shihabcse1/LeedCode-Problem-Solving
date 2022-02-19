# Problem Link: https://leetcode.com/problems/search-insert-position/
# Runtime: 52ms, Memory: 14.8 MB

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        high = len(nums) - 1
        low = 0
        
        while low <= high:
            mid = low + ((high - low) // 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
                    
        return low
                