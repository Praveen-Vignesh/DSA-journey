#include <iostream>
#include <vector>

bool validAnagram(std::string s1, std::string s2){
    if(s1.size() != s2.size()){
        return false;
    }
    // here my first thought was to create an array that will contian each caharacter of the string
    // and while iterating through the sencond string we fill searchg and find the character in the array
    // if present we delete that if not return false and after completing if the array has elements left return false

    //but thats not really a fast solution becasue we need to search through the aray and delete n number of times

    // Instead create a frequency arry for the characters (26 if only lowercase 52 if both upper and lower)
    // increment 1 for every character in string 1 in their corresponding array index (string1[i] - 'a')
    //                                                                             eg:  'e' - 'a' => 4
    // decrement by 1 for every character in string 2 in their corespoding array index

    std::vector<int> count(26, 0);
    for (int i = 0; i < s1.size(); i++){
        count[s1[i] - 'a'] += 1;
        count[s2[i] - 'a'] -= 1;
    }

    for (int i = 0; i < 26; i++){
        if(count[i] != 0){
            return false;
        }
    }
    
    return true;
}

int main()
{
    std::string s1 = "racecar";
    std::string s2 = "carrace"; //valid anagram

    std::string t1 = "acc";
    std::string t2 = "ac"; //invalid anagram
}
