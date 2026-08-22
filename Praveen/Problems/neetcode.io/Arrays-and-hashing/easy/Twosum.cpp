#include <iostream>
#include <vector>
#include <unordered_map>

int main(){
    std::vector<int> nums = {2, 3, 4, 5};
    int target = 5;

    int n = nums.size();
    std::unordered_map<int, int> hashMap;

    for (int i = 0; i < nums.size(); i++){
        int diff = target - nums[i];
        if(hashMap.find(diff) != hashMap.end()){
            std::cout << hashMap[diff] << " " << i << std::endl;
            return 0;
        }
        hashMap[nums[i]] = i;
    }
    std::cout << "No solution" << std::endl;
    return 0;
}