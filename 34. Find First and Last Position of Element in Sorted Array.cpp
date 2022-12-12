class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {

        vector<int> arr; 
        arr.push_back(find_start_index(nums, target));
        arr.push_back(find_end_index(nums, target));
        
        return arr;
    }

    int find_start_index(vector<int>& nums, int target){

        int start = 0;
        int end = nums.size() - 1;
        int position = -1;

        while(start <= end) {
            int mid = (start + end) / 2;
            if(nums[mid] > target) {
                end = mid - 1;
            }else if(nums[mid] < target) {
                start = mid + 1;
            }else {
                position = mid;
                end = mid - 1;
            }
        }
        return position;
    }

     int find_end_index(vector<int>& nums, int target){

        int start = 0;
        int end = nums.size() - 1;
        int position = -1;

        while(start <= end) {
            int mid = (start + end) / 2;
            if(nums[mid] > target) {
                end = mid - 1;
            }else if(nums[mid] < target) {
                start = mid + 1;
            }else {
                position = mid;
                start = mid + 1;
            }
        }
        return position;
    }

};