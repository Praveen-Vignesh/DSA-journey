#include <iostream>
#include <vector>

using namespace std;

int main(){
    std::vector<std::string> strs = {"bat", "bag", "batman", "bankai"};

    // Lexicographical Sorting
    // When u sort the array in lexicographical wise and compare the two extreme ends
    // if the two extreme ends happens to have ths same prefix then all other elements inbetween should also have the same prefix right ?
    // and lets say we find a point where the prefix stop matching between the first and the last element
    // now lets call this point X
    // and when we reach point X we also know that all other elements have the same prefix as point X because this is lexical sorted array
    // Now we can just simple return the substr of the first string up untill point X

    // eg: [bat, bag, batman]
    // sorted form will be [bag, batman, bat]
    // we need to compare bag and batman , and we have the same prefix until "ba"
    // when we try to compare strs[0][2] with strs.end()[2] they are not matching but we know the other elements also have the same prefix untill this point
    // so we can return the prefix as the string until untill index 1 "ba"

    // now this would take O(m * n log n)   

    // standard O(n*n) method
    // where we take one element (first) and compare every character of it to the rest of the strings
    // this is much optimal

    for (int i = 0; i < strs[0].length(); i++){
        for (int j = 1; j < strs.size(); j++){
            if(i >= strs[j].length() || strs[j][i] != strs[0][i]){
                cout << strs[0][i - 1];
                return 0;
            }
        }
    }

    cout << strs[0];
    return 0;
}
    