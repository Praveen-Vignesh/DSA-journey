// Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.
// An anagram is a string that contains the exact same characters as another string,
// but the order of the characters can be different.

#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

int main(){
    vector<string> strs = {"act","pots","tops","cat","stop","hat"};

    unordered_map<string, vector<string>> hashMap;

    for(int i = 0; i < strs.size(); i++){
        vector<int> freq(26, 0);

        for(int j = 0; j < strs[i].length(); j++){
            freq[strs[i][j] - 'a']++;
        }

        string key = to_string(freq[0]);

        for(int k = 1; k < 26; ++k){
            key += ',' + to_string(freq[k]);
        }
        hashMap[key].push_back(strs[i]);
    }

    vector<vector<string>> result;

    for(const auto& pair: hashMap){
        result.push_back(pair.second);
    }
    for(const auto& element: result){
        cout << "[";
        for(size_t i = 0; i < element.size(); ++i){
            cout << element[i];
            if(i + 1 < element.size()) cout << ", ";
        }
        cout << "]\n";
    }
    
    return 0;
}