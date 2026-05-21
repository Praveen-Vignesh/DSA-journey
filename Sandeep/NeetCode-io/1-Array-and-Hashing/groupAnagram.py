def groupAnagrams_pythonic(strs: List[str]) -> List[List[str]]:
    """
        This is slow and exceeds the time limit
    """
    result = []
    def isAnagram(left, right):
        return sorted(left) == sorted(right) 
    
    for i in strs:
        mark = []
        for j in strs:
            if isAnagram(i, j):
                mark.append(j)
        if mark not in result:
            result.append(mark)
    return result

## I have to do some digging and found this "collection" module, I can this is so much handy and nice to use
from collections import defaultdict

def groupAnagrams_hashtable(strs: List[str]) -> List[List[str]]:
    """
        Uses a hashtable as a key to keep counts of the words with same hashtables
        Args:
        - strs (List[str]): list of strings to be tested on
        
        Returns:
        - List[List[str]]: list made of lists words those are anagrams to each other as an element in this 
    """
    anagrams = defaultdict(list)
    for word in strs:
        count = [0] * 26 # the hash table here in
        for ch in word:
            count[ord(ch) - ord('a')] += 1   # maps the alphabets 'a' to 0, 'b' to 1, etc.
        key = tuple(count)   # hashtable in tuple
        anagrams[key].append(word) # as count hashtable is used as a key we can see add values the words, and as their 
        # keys would match they would blend into few lists to collect up
    return list(anagrams.values())

print(groupAnagrams_hashtable(["eat","tea","tan","ate","nat","bat"]))