def containsDuplicate(nums: List[int]) -> bool:
    
    ## ---- Pythonic way ----
    # 1. Turn the list given into a set()
    # 2. Store it in a variable
    # 3. Compare the lengths of them
        # 3.1, If u find it then return False
        # 3.2. Else return True
    
    set_nums = set(nums)
    return len(set_nums) < len(nums)
