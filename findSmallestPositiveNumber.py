# You are given an unsorted array with both positive and negative elements. 
# You have to find the smallest positive number missing from the array in
# O(n) time using constant extra space. You can modify the original array.

# [3, 4, 7, 1]
# [1, 3, 4, 7]

def smallestPositiveNumber(arr):
    arr.sort()

    temp = arr[0]

    containsZero = False

    if temp < 0:
        containsZero = True

    for num in arr:
        if num - temp == 1:
            temp = num
            continue
        if num > temp:
            if temp + 1 < 0:
                continue
            return temp + 1
    return temp + 1



print(smallestPositiveNumber([2, 3, -7, 6, 8, 1, -10, 15]))
