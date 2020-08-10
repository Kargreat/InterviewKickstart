ip_ = [2, 1, 4, 5, 3, 192, 189, 205, 204]


def quick(arr, start, end):
    if start >= end:
        return arr

    # call this the pivot element
    mid = len(arr) // 2

    # swapping start element and pivot element
    temp = arr[0]
    arr[0] = arr[mid]
    arr[mid] = temp

    # set the loop variables
    smaller = start

    for bigger in range(start, end):
        if arr[bigger] < arr[start]:
            smaller += 1
            temp = arr[bigger]
            arr[bigger] = arr[smaller]
            arr[smaller] = temp

    temp = arr[0]
    arr[0] = arr[smaller]
    arr[smaller] = temp
    print(arr)
    quick(arr, 0, smaller - 1)
    quick(arr, smaller + 1, end)


def quick_sort(arr):
    if len(arr):
        return arr
    else:
        quick(arr=arr, start=0, end=len(arr))


if __name__ == '__main__':
    print(quick_sort(arr=[3, 1, 4]))