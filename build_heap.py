# python3


def build_heap(data):
    swaps = []
    n = len(data)
    # TODO: Creat heap and heap sort
    for i in range(n // 2, -1, -1):
        swaps = sift_down(data, swaps, i, n)
    return swaps


def sift_down(data, swaps, i, n):
    while i<n:
        left = 2 * i + 1
        right = 2 * i + 2
        smallest = i
        if left < n and data[left] < data[smallest]:
            smallest = left
        if right < n and data[right] < data[smallest]:
            smallest = right
        if smallest != i:
            data[i], data[smallest] = data[smallest], data[i]
            swaps.append((i, smallest))
            i = smallest
        else:
            break
    return swaps


def main():
    
    # add input for I or F 
    heap_type = input().strip().upper()
    assert heap_type in ["I", "F"]

    # TODO : add input and corresponding checks
    n = int(input())
    assert 1 <= n <= 10**5
    data = list(map(int, input().split()))

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    print(len(swaps))
    # this number should be less than 4n (less than 4*len(data))

    # output all swaps
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
