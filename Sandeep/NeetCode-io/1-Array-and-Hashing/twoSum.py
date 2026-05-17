def twoSum_quick(nums: List[int], target: int) -> List[int]:
    want = []
    for i in range(len(nums)):
        # index = i belongs to 'nums'
        # we need this to be in the list
        y = target - nums[i]
        if y in nums:
            # avoiding considering the same number 2 times
            if i != nums.index(y):
                want.append(i)
                want.append(nums.index(y))
                return want

def twoSum_hashmap(nums: List[int], target: int) -> List[int]:
    seen = {} 
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        # counting stops if it sees a complement in the dictionary
        # counting only happens if no complement in sight
        seen[num] = i
