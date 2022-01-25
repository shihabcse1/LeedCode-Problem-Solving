class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        list_length = len(nums);
        for i in range(0, list_length):
            for j in range(i+1, list_length):
                if (nums[i] + nums [j] == target):
                    return i, j