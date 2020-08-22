ip_ = [2, 1, 4, 5, 3, 192, 189, 205, 204]
l = [2, 192, 205, 5]
r = [1, 189, 4, 204]


def merge(left: list, right: list) -> list:
    i = j = 0
    op_ = list()
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            op_.append(left[i])
            i += 1

        else:
            op_.append(right[j])
            j += 1

    if i < len(left):
        while i < len(left):
            op_.append(left[i])
            i += 1

    if j < len(right):
        while j < len(right):
            op_.append(right[j])
            j += 1

    return op_


def mergesort(ip: list) -> list:
    if len(ip) > 1:
        mid = len(ip) // 2
        l = ip[:mid]
        r = ip[mid:]
        mergesort(l)
        mergesort(r)
        values = []

        i = j = k = 0

        while i < len(l) and j < len(r):
            if l[i] <= r[j]:
                ip[k] = l[i]
                values.append(l[i])
                i += 1
            else:
                ip[k] = r[j]
                values.append(r[j])
                j += 1
            k += 1
        while i < len(l):
            values.append(l[i])
            ip[k] = l[i]
            i += 1
            k += 1

        while j < len(r):
            ip[k] = r[j]
            values.append(r[j])
            j += 1
            k += 1
        # print(ip)
        return values

no_ip = []



if __name__ == '__main__':
    test = [1, 2, 4, 5, 6]
    # print(ip_)
    # print('values:%s', mergesort(ip_))

