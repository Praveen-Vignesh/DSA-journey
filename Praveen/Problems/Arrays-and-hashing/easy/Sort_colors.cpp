/*

You are given an array nums consisting of n elements where each element is an integer representing a color:

0 represents red
1 represents white
2 represents blue

Your task is to sort the array in-place such that elements of the same color are grouped together and arranged in the order: 
red (0), white (1), and then blue (2).

*/



/*
I have used count sort here
the idea is that since we only have three posssible valu
*/


#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    void sortColors(vector<int>& nums) {
        vector<int> count(3);

        for(int& num : nums){
            count[num]++;
        }

        int index = 0;

        for(int i = 0; i <  3; i++){
            while(count[i] > 0){
                nums[index] = i;
                index++;
                count[i]--;
            }
        }
    }
};