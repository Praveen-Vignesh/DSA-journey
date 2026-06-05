#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        int n = nums.size();
        int i = 0;

        while(i < n){
            if (nums[i] <= 0 || nums[i] > n || nums[i] == nums[nums[i] - 1]){
                i++;

            }
            else if(nums[i] != i+1){
                int temp = nums[nums[i] - 1];
                nums[nums[i] - 1] = nums[i];
                nums[i] = temp;

            }
            else{
                i++;
            }
        }

        for(int i = 0; i < n; i++){
            if(nums[i] != i+1){
                return i+1;
            }
        }

        return n+1;
    }
};

int main() {
    vector<int> nums = {-1, -2, 1000, 0, 3, 4, 5};
    int test = Solution().firstMissingPositive(nums);
    cout << test;
    return 0;
}
