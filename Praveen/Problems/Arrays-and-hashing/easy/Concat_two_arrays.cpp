/*
    Question:

    You are given an integer array nums of length n.
    Create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
    Specifically, ans is the concatenation of two nums arrays.
    
*/

#include <iostream>
#include <vector>

std::vector<int> getConcatenation(std::vector<int>& nums) {
        std::vector<int> result;
        for(int j = 0; j < 2; j++){
            for(int i = 0; i < nums.size(); i++){             
                result.push_back(nums[i]);
            }
        }
        return result;


        // std::vector<int> result = nums;
        // result.insert(result.end(), nums.start(), nums.end());

}
    
int main(){
    return 0;
}