#include <iostream>
#include <vector>
#include <unordered_map>

int main(){
    std::vector<int> nums = {2, 3, 4, 5};
    int target = 5;

    int n = nums.size();
    std::unordered_map<int, int> prevMap;

    for (int i = 0; i < n; i++) {
        int diff = target - nums[i];
        if (prevMap.find(diff) != prevMap.end()) {
            std::cout << prevMap[diff] << " " << i << '\n';
            return 0;
        }
        prevMap.insert({nums[i], i});
    }
    return 0;
}