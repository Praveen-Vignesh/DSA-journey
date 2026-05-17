/*
    Question:

    Given an integer array nums, 
    return true if any value appears more than once in the array, 
    otherwise return false.

*/

#include <iostream>
#include <unordered_set>

int main(){
    std::vector<int> nums = {1, 2, 3, 2, 3, 1, 4, 5, 6};

    std::unordered_set<int> hashset;
    for(int i = 0; i < nums.size(); i++){
        hashset.insert(nums[i]);
    }

    return hashset.size() != nums.size() ? true : false; //remember the question is to check for duplicates not uniqueness so != is used instead of ==
}