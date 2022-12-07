class Solution {
    
    List<List<Integer>> result = new ArrayList();
    
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        int arr_len = nums.length;
        int target = 0;
        
        for(int i = 0; i < arr_len; i++){
            // check a is duplicate or not. Ex: a + b + c = 0
            if(i == 0 || nums[i-1] != nums[i]) {
                // target = 0 - a
                twoSumSorted(i+1, arr_len - 1, nums, 0-nums[i]);
            }
        }
        return result;
    }
    
    public void twoSumSorted(int i, int j, int nums[], int target) {
        
        int a = nums[i-1];
        
        while(i < j) {
            if(nums[i] + nums[j] > target) {
                j--;
            } else if(nums[i] + nums[j] < target) {
                i++;
            } else {
                List<Integer> items = new ArrayList();
                items.add(a);
                items.add(nums[i]);
                items.add(nums[j]);
                result.add(items);
                
                // skip duplicate b
                // check whether out of range by i < j
                while(i < j && nums[i] == nums[i+1]){
                    i++;
                }
                
                // skip duplicate b
                // check out of range by i < j
                while(i < j && nums[j-1] == nums[j]){
                    j--;
                }
                
                i++;
                j--;
            }
        }
        
    }
    
}