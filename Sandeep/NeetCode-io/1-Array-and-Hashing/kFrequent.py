def topKFrequent_pythonic(nums: List[int], k: int) -> List[int]:
    # Step 1: Count frequencies
    counter_dict = {}
    for num in nums:
        counter_dict[num] = counter_dict.get(num, 0) + 1
    
    # Step 2: Sort by frequency descending
    sorted_items = sorted(counter_dict.items(), key=lambda x: x[1], reverse=True)
    
    # Step 3: Take top k keys
    result = [item[0] for item in sorted_items[:k]]

    return result

print(topKFrequent_pythonic(nums = [1,1,1,2,2,3], k = 2))