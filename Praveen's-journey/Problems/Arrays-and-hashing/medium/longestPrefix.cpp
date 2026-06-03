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
    // sorted form will be [bag,batman bat, ]
    // we need to compare bag and batman , and we have the same prefix until "ba"
    // when we try to compare strs[0][2] with strs.end()[2] they are not matching but we know the other elements also have the same prefix untill this point
    // so we return substr strs[0] (0, i) where i == 2

    