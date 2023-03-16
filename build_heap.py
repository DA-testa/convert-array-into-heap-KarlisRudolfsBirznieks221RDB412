# python3
# 221RDB412 Kārlis Rūdolfs Birznieks

def build_heap(data):
    swaps = []
    n = len(data)
    # TODO: Create heap and heap sort
    for i in range(n // 2, -1, -1):
        swaps = sift_down(data, swaps, i, n)
    return swaps


def sift_down(data, swaps, i, n):
    while i < n:
        left = 2 * i + 1
        right = 2 * i + 2
        smallest = i
        if left < n and ((data[left] < data[smallest]) if heap_type == "I" else (data[left] > data[smallest])):
            smallest = left
        if right < n and ((data[right] < data[smallest]) if heap_type == "I" else (data[right] > data[smallest])):
            smallest = right
        if smallest != i:
            data[i], data[smallest] = data[smallest], data[i]
            swaps.append((i, smallest))
            i = smallest
        else:
            break
    return swaps


def main():
    # Add input for I or F 
    global heap_type
    heap_type = input().strip().upper()
    assert heap_type in ["I", "F"]

    # Add input for n
    n = int(input().strip())
    assert 1 <= n <= 10**5

    # Add input for data and split it by spaces
    data = list(map(int, input().strip().split()))
    assert len(data) == n

    # Call function to assess the data and give back all swaps
    swaps = build_heap(data)

    # Output the heap type and how many swaps were made
    print(heap_type)
    print(len(swaps))

    # Output all swaps
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
