class Solution {
public:
    int findUnsortedSubarray(vector<int>& nums) {

        vector<int> sorted_nums = nums;
        int nums_length = nums.size();
        int left = 0;
        int right = 0;

        sort(sorted_nums.begin(), sorted_nums.end());

        // finding first index of unsorted
        for(int i = 0; i < nums_length; i++) {
            if(nums[i] != sorted_nums[i]){
                left = i;
                break;
            }
        }

        // finding last index of unsorted
        for(int i = nums_length-1; i >= 0; i--) {
            if(nums[i] != sorted_nums[i]){
                right = i;
                break;
            }
        }

        if(left == 0 && right == 0) {
            return 0;
        } else {
            return right + 1 - left;
        }

    }
};