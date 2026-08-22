/*

    Given an array nums of size n, return the majority element.
    The majority element is the element that appears more than ⌊n / 2⌋ times in the array.
    may assume that the majority element always exists in the array.

*/

// now this problem can be tackled with hashmap or using sorting or counting if a value is more the lenght/2

// but i am going to solve this using Boyer-Moore voting algorithm just to get the hang of it


/* ## Boyer-moore voting algorithm
        the Boyer-Moore algorithm works by maintaining a candidate and a count.
        When we see the candidate, we increment the count; otherwise, we decrement it.
        When the count reaches 0, we pick a new candidate.
        Since the majority element appears more than half the time, it will survive this elimination process and remain as the final candidate.
*/

#include <iostream>
#include <vector>

using namespace std;


int main(){
    vector<int> nums = {1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4};

    int candidate;
    int count = 0;

    for(const int num: nums){
        if(count == 0){
            candidate = num;
        }
        count += (num == candidate) ? 1 : -1;
    }

    return candidate;
}