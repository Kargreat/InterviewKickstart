import heapq

ip_ = [2, 1, 4, 5, 3, 192, 189, 205, 204]


def heapsort(arr: list):
    heap = []
    for i in arr:
        heapq.heappush(heap, i)

    return [heapq.heappop(heap) for i in range(0, len(heap))]


if __name__ == '__main__':
    print(ip_)
    print(heapsort(ip_))

