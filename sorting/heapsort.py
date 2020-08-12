import heapq
ip_ = [4, 3, 1, 8, 10, 7, 11, 15, 13, 12, 6, 55]


def heapsort(ip: list):
    heap = []
    for i in ip:
        heapq.heappush(heap, i)

    return [heapq.heappop(heap) for i in range(0, len(heap))]


if __name__ == '__main__':
    print(heapsort(ip_))
