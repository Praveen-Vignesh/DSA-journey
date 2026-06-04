/*
    Given an integer array nums and an integer k, return the k most frequent elements within the array.
    The test cases are generated such that the answer is always unique.
    You may return the output in any order.

*/

/*
    we are here using something called bucker sorting : were we put elements of a certain group into a vertain index of a vector 
    this certain index acts like a bucket

    in this problem we first create a hash map that tracks all the freq of all the element
    then iterate through the hashmap
    the value (actual frequency) is the index of the new vector
    the key (number with that frequency) is pushed to the index (that index is another vector of ints)

    now for eg:
    if array is {1, 1, 1, 2, 2, 3, 3}

    then the freq vector will be like {, {2, 3}, {1}}

    then we can iterate from the last element of the freq array untill we get k numbers and return them
*/


#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> count;
        vector<vector<int>> freq(nums.size()+1);

        for(int n: nums){
            count[n] = 1 + count[n];
        }

        for(const auto& entry: count){
            freq[entry.second].push_back(entry.first);
        }

        vector<int> result;

        for(int i = freq.size()-1; i > 0; --i){
            for(int n: freq[i]){
                result.push_back(n);
                if(result.size() == k){
                    return result;
                }
            }
        }

        return result;
    }
};