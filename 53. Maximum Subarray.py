# Time Complexity: O(n) * O(n) * O(n) = O(n)^3
# Space Complexity: O(1) Because we didn't use any extra array. Just used 5 variables.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -100000
        list_len = len(nums)
        for i in range(1, list_len+1): # O(n)
            for j in range(list_len-i+1): # O(n)
                sum_ = sum(nums[j:j+i]) # O(n)
                if max_sum < sum_:
                    max_sum = sum_
                    
        return max_sum


# Accepted Solution
# Time Complixity: O(n)

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        temp = [nums[0]]
        current_sum = nums[0];
        list_len = len(nums)
        for i in range(1, list_len):
            if current_sum + nums[i] > nums[i]: 
                current_sum = current_sum + nums[i]
            else:
                current_sum = nums[i]
            
            temp.append(current_sum)
                    
        return max(temp)
