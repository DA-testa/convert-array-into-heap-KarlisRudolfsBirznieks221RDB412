# python 3
# 221RDB412 Kārlis Rūdolfs Birznieks

import os

def build_heap(data):
    swaps = []
    n = len(data)
    # TODO: Create heap and heap sort
    
    # Add heap_type parameter to sift_down function
    for i in range(n // 2, -1, -1):
        swaps = sift_down(data, swaps, i, n, heap_type)
    return swaps


def sift_down(data, swaps, i, n, heap_type):
    while i < n:
        left = 2 * i + 1
        right = 2 * i + 2
        smallest = i
        # Modify the comparison based on the heap_type parameter
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
 
    global heap_type
   
    heap_type = input().strip().upper()
    assert heap_type in ["I", "F"]

    # Read input
    if heap_type == "F":
        # Input from file
        try:
            # Prompt user for file path and strip the carriage return character
            file_path = input("Input file path: ").rstrip('\r')
            # Use os to get the absolute path of the file
            abs_path = os.path.abspath(file_path)
            # Read input from file
            with open(abs_path, "r") as file:
                # Read the number of elements from the first line
                n = int(file.readline().strip())
                # Read the list of elements from the second line
                data = list(map(int, file.readline().strip().split()))
        except FileNotFoundError:
            print("File not found.")
            return
    else:
        # Input from keyboard
        try:
            # Read the number of elements from the first line
            n = int(input().strip())
            # Read the list of elements from the second line
            data = list(map(int, input().strip().split()))
        except ValueError:
            print("Invalid input format.")
            return

    # Check input length
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
