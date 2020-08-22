ip_ = [2, 1, 4, 5, 3, 192, 189, 205, 204]

def merge_sort(arr: list):
    if len(arr) == 1:
        return arr
    else:
        l = arr[:int(len(arr)/2)]
        r = arr[int(len(arr)/2):]
        merge_sort(l)
        merge_sort(r)

        i = j = k = 0
        while i < len(l) and j < len(r):
            if l[i] <= r[j]:
                arr[k] = l[i]
                i += 1
            else:
                arr[k] = r[j]
                j += 1
            k += 1

        while i < len(l):
            arr[k] = l[i]
            i += 1
            k += 1
        while j < len(r):
            arr[k] = r[j]
            j += 1
            k += 1

        return arr


if __name__ == '__main__':
    print(ip_)
    print(merge_sort(ip_))
