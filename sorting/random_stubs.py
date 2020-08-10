from random import random

ip_ = [6, 4, 3, 8, 1, 5, 2, 7]

# Algo:
# for an array of size N, keep paritioning the array between two halves, left and right. recursively call the algorithms
#     for the left and right. Then when the size becomes one return. Now in the returned arrays, merge two array.
#     I know what I need to do there.


def bubblesort(a):
    for start in range(len(a)):
        for i in range(len(a)-1,start,-1):
            if a[i-1] > a[i]:
                (a[i-1],a[i]) = (a[i],a[i-1])


def insertionsort(A, n):
    if n <= 1:
        return False
    for i in range(2, n):
        ith = A[i]
        j = i-1
        while j >= 1 and A[j] > ith:
            A[j+1] = A[j]
            j = j - 1
        A[j+1] = ith
    return True


def msort(l, start, end):
    if start >= end:
        return
    mid = (start + end) / 2
    msort(1, start, mid)
    msort(1, mid+1, end)

    i = start
    j = mid + 1
    mlist = []

    while i <= mid and j <= end:
        if l[i] <= l[j]:
            mlist.append(l[i])
            i += 1
        elif l[j] < l[i]:
            mlist.append(l[j])
            j += 1
        while i <= mid:
            mlist.append([i])
            i += 1
        while j <= end:
            mlist.append(l[j])
            j += 1
        l[start:end+1] = mlist

def qsort(l, start, end):
    if start >= end:
        return
    # Pick a random element as pivot
    randindex = random.randint(start,end)
    (l[randindex],l[start]) =(l[start],l[randindex])
    pivot = l[start]
    smaller = start
    bigger = start
    for bigger in range(start+1, end+1):
        if l[bigger] <= pivot:
            smaller += 1
            (l[smaller], l[bigger]) = (l[bigger],l[smaller])
    # Place pivot in the right spot
    (l[start],l[smaller]) = (l[smaller],l[start])
    qsort(l, start, smaller - 1)
    qsort(l, smaller + 1, end)


ip_ = ['G', 'B', 'G', 'G', 'R', 'B', 'R', 'G']


def dutch_flag_sort():
    balls = ['G', 'B', 'G', 'G', 'R', 'B', 'R', 'G']
    i = 0
    j = 0
    k = len(balls)

    while j < k:
        if balls[j] == 'R':
            c = balls[i]
            balls[i] = balls[j]
            balls[j] = c
            i += 1
            j += 1

        elif balls[j] == 'B':
            print(False)
            k = k - 1
            c = balls[k]
            balls[k] = balls[j]
            balls[j] = c
        else:
            print('equal')
            j = j + 1

    return balls


def swap(a, b):
    c = b
    b = a
    a = c
    return a, b


def merge_two_sorted():
    arr1 = [1, 10, 11, 12, 13]
    arr2 = [2, 3, 4, 13, 15, 0, 0, 0, 0, 0]
    arr1_index = len(arr1) - 1
    arr2_index = arr1_index
    max_index = len(arr2) - 1
    while arr1_index > -1 and arr2_index > -1:
        if arr1[arr1_index] > arr2[arr2_index]:
            arr2[max_index] = arr1[arr1_index]
            arr1_index = arr1_index - 1
            max_index = max_index - 1

        elif arr1[arr1_index] < arr2[arr2_index]:
            arr2[max_index] = arr2[arr2_index]
            arr2_index = arr2_index - 1
            max_index = max_index - 1

        elif arr1[arr1_index] == arr2[arr2_index]:
            arr2[max_index] = arr2[arr2_index]
            arr2_index = arr2_index - 1
            max_index = max_index - 1
            arr2[max_index] = arr1[arr1_index]
            arr1_index = arr1_index - 1
            max_index = max_index - 1

    if arr2_index == -1 and arr1_index == 0:
        arr2[0] = arr1[0]

    return arr2


if __name__ == '__main__':
    print(merge_two_sorted())
