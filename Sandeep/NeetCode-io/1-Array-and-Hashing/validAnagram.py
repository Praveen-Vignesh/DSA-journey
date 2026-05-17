def isAnagram_quick(s: str, t: str) -> bool:
    ## ---- Quick thinking ----
    # 1. Sort both the strings
    # 2. Compare if they are same or not
        # 3.1, If u find it then return False
        # 3.2. Else return True
    if len(s) != len(t):
        return False

    sorted_s = sorted(s)
    sorted_t = sorted(t)

    return sorted_s == sorted_t

def isAnagram_hash(s: str, t: str) -> bool:
    ## ---- Using Hashmaps ----
    ## 0. Initial Check
    if len(s) != len(t):
        return False

    ## 1. creating a dictionary for occurances for 's' string
    s_char_dict = {}
    for char in s:
        if char not in s_char_dict:
            s_char_dict[char] = 0
        s_char_dict[char] += 1

    ## 2. subtract instances from the 's' dictionary for occurances for 't' string
    for char in t:
        if char not in s_char_dict:
            return False
        s_char_dict[char] -= 1
        if s_char_dict[char] < 0:
            return False


    return True

