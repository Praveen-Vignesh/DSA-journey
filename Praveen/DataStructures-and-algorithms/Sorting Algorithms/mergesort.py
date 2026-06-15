def merge(nums, left, mid, right):

    leftArr = nums[left: mid+1]
    rightArr = nums[mid+1: right+1]


    ptr1, ptr2 = 0, 0
    curr = left

    while ptr1 < mid - left + 1 and ptr2 < right - mid:
        if leftArr[ptr1] < rightArr[ptr2]:
            nums[curr] = leftArr[ptr1]
            ptr1+=1
        else:
            nums[curr] = rightArr[ptr2]
            ptr2+=1
        
        curr+=1
    

    while(ptr1 < mid - left +1):
        nums[curr] = leftArr[ptr1]
        ptr1+=1
        curr+=1
    
    while(ptr2 < right - mid):
        nums[curr] = rightArr[ptr2]
        ptr2+=1
        curr+=1
    

    return


def mergeSort(nums, left, right): # [2,1,3,5,4,6]
    if (left >= right): return

    mid =  left + (right - left) // 2
    
    mergeSort(nums, left, mid) #left branch
    mergeSort(nums, mid+1, right) # right branch

    merge(nums, left, mid, right)


nums = [4,2,1,6,3,7,8,0]
mergeSort(nums, 0, 7)

print(nums)