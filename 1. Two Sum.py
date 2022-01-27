class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        lenth = len(nums)
        for i in range(lenth):
            key = target - nums[i]
            if key in hashmap:
                return [i, hashmap[key]]
            hashmap[nums[i]] = i