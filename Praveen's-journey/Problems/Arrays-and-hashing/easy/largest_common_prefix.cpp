// You are given an array of strings strs. Return the longest common prefix of all the strings.
// If there is no longest common prefix, return an empty string "".

// Approach 1: take one element as refercne and compare all other strings (O(n*m))
// APproach 2; sort the array in lexicographical format then compare and first and last element 
//              this works because if the las element matches completely with the first element lets say untill index 3 then all other elements before that also matches the prefix


// but sorting this in lexicographical gives O(m * nlog n)
// this is significantly worse than the O(n*m)')
#include <iostream>
#include <vector>
#include <string>

using namespace std;

string findPrefix(vector<string> words){

    string refWord = words[0];
    string result;

    for (int i = 0; i < words[0].length(); i++){

        for (int j = 1; j < words.size(); j++){

            if(i >= words[j].length() || refWord[i] != words[j][i]){

                result = refWord.substr(0, i);
                return result;
            }
        }
        result = refWord.substr(0, i);
    }

    return result;
}

int main(){
    vector<string> words = {"dance", "dag", "danger", "damage"};
    
    string result = findPrefix(words);

    cout << result;

    return 0;
}