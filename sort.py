def selectsort(nums):
    for i in range(len(nums)-1):
        k = i
        for j in range(i+1,len(nums)):
            if nums[j] < nums[k]:
                k = j
        nums[i],nums[k] = nums[k],nums[i]
    return nums


def bubblesort(nums):
    n = len(nums)
    for i in range(n-1,0,-1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
    return nums

def partition(nums,left,right):
    tmp = nums[left]
    while left < right:
        while nums[right] >= tmp and left < right:
            right-=1
        nums[left] = nums[right]
        while nums[left] <= tmp and left < right:
            left+=1
        nums[right] = nums[left]
    nums[left] = tmp
    return left



def quicksort(num,left,right):
    if left < right:
        mid = partition(num,left,right)
        quicksort(num,left,mid)
        quicksort(num,mid+1,right)

