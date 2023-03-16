# python3


def build_heap(data):
    swaps = []
    n = len(data)
    for i in range(n // 2, -1, -1):
        swaps = sift_down(data, swaps, i, n)
    return swaps


def sift_down(data, swaps, i, n):
    while i < n:
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
    # Get the heap type input and validate it
    heap_type = input().strip().upper()
    assert heap_type in ["I", "F"]

    # Get the number of elements in the data list and validate it
    n = int(input().strip())
    assert 1 <= n <= 10**5

    # Get the list of data elements and validate it
    data = list(map(int, input().strip().split()))
    assert len(data) == n

    # Call the build_heap function to generate swaps and print the results
    swaps = build_heap(data)
    print(heap_type)
    print(str(len(swaps)))
    for swap in swaps:
        print(str(swap[0]) + " " + str(swap[1]))


if __name__ == "__main__":
    main()
