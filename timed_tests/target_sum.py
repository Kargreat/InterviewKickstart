n = 3
k = 6
array = [2, 4, 8]


def check_if_sum_possible(arr, k):
    partial_sum = 0
    return target_sum(arr, k, len(arr), partial_sum)


def target_sum(arr, k, n, partial_sum):
    if len(arr) == 0 and partial_sum == k:
        return True
    else:
        return 1


if __name__ == '__main__':
    print(check_if_sum_possible(array, k))