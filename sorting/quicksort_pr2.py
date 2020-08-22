ip_ = [2, 1, 4, 5, 3, 192, 189, 205, 204]


def quick(arr, start, end):
    if start >= end:
        return arr

    mid = (start + end) // 2
    temp = arr[0]
    arr[0] = arr[mid]
    arr[mid] = temp

    smaller = start
    for bigger in range(start, end):
        if arr[bigger] < arr[start]:
            smaller += 1
            temp = arr[smaller]
            arr[smaller] = arr[bigger]
            arr[bigger] = temp

    # swap the start and smaller element
    tmp = arr[0]
    arr[0] = arr[smaller]
    arr[smaller] = tmp

    quick(arr, 0, smaller)
    quick(arr, smaller+1, end)
    return arr


def qsort(arr: list):
    if len(arr) == 1:
        return arr
    else:
        return quick(arr, 0, len(arr))


if __name__ == '__main__':
    print(qsort(ip_))


