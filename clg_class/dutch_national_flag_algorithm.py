# take 3 variables low,high,mid
# low & mid in 0 index
# high at last index
# if mid is 0 swap low & mid and low++, mid++
# if mid is 1 mid++
# if mid is 2 swap mid & high and high--


arr = [2,0,2,1,1,0]

len = len(arr)
high = len-1
low = mid = 0
while mid <= high:
    if arr[mid] == 0:
        arr[low],arr[mid] = arr[mid],arr[low]
        low += 1
        mid += 1
    elif arr[mid] == 1:
        mid += 1
    else:
        arr[mid],arr[high] = arr[high],arr[mid]
        high -= 1

print(arr)

