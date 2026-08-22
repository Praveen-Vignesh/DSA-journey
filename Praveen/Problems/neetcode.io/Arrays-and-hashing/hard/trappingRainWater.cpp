#include <iostream>
#include <vector>
using namespace std;

// I attempted to solve this using O(n) time completexity 
// at first i used one while loop and split the problem into two 
// part one (the main part): calculate the number of water between two walls when wall2  > wall1 and update wall1 = wall2
// part two sometimes we never find wall2 > walll 1 but we will com across valid pools of water where wall2 < wall1
// now i cant do the same calculation and updation from wall1 = wall2 for every wall2 < wall 1
// this will make me miss the count of water blocks when i eventually find a wall2 > wall1

// so i sued a temp water to keep track of the total water blocks i find for every wall2 < wall1 
// this failed to give me the correct count because of some counting problem with tempwater (it sometimes gets overwriten to 0)


// so this new idea works its the same idea but instead of 1 pass but checking for two conditions
// i split the two conitions into two passes so its essentially the part one (main part) calculation (which works perfectly) but in left to right and right to left order
int main(){
    vector<int> height = {0,2,0,3,1,0,1,3,2,1};
    int n = height.size();
    int wall1 = -1;
    int wall2 = -1;
    int water = 0;
    vector<int> prefixSum;

    for (int i = 0; i < n; i++)
    {
        if (i == 0)
        {
            prefixSum.push_back(height[i]);
            continue;
        }
        prefixSum.push_back(height[i] + prefixSum[i - 1]);
    }
    // First we go from left to right and calculate the number of water only when we keep on finding walls greater in height to the right of wall 1

    wall1 = 0;
    for(int i = 1; i < n; i++){
        if(height[i] >= height[wall1]){
            int waterContent = std::min(height[wall1], height[i]) * (i - wall1 - 1);
            int noofWalls = prefixSum[i - 1] - prefixSum[wall1];
            waterContent -= noofWalls;
            water += waterContent;
            wall1 = i;
        }
    }
    // next we go from right to left and calculate the number of water only when we find walls that are greater in height to the left of wall 1
    wall2 = n - 1;
    for(int i = n - 2; i >= wall1; i--){
        if(height[i] >= height[wall2]){
            int waterContent = std::min(height[wall2], height[i]) * (wall2 - i - 1);
            int noofWalls = prefixSum[wall2 - 1] - prefixSum[i];
            waterContent -= noofWalls;
            water += waterContent;
            wall2 = i;
        }
    }

    return water;
}