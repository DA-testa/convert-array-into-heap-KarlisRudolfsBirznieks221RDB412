# 221RDB412 Kārlis Rūdolfs Birznieks

def build_heap(data):
    swaps = []
    n = len(data)
    # Create heap
    for i in range(n//2, -1, -1):
        sift_down(i, data, swaps)
    return swaps

def sift_down(i, data, swaps):
    n = len(data)
    min_index = i
    l = 2*i + 1
    if l < n and data[l] < data[min_index]:
        min_index = l
    r = 2*i + 2
    if r < n and data[r] < data[min_index]:
        min_index = r
    if i != min_index:
        swaps.append((i, min_index))
        data[i], data[min_index] = data[min_index], data[i]
        sift_down(min_index, data, swaps)

def main():
    # Prompt user for input type (F for file, I for keyboard)
    option = input("Enter input type: ")
    data = []

    if "F" in option:
        # Input from file
        try:
            file_path = input("Input file path: ")
            with open(f"tests/{file_path}", "r") as file:
                n = int(file.readline().strip())
                data = list(map(int, file.readline().strip().split()))
        except FileNotFoundError:
            print("File not found.")
            return
    elif "I" in option:
        # Input from keyboard
        try:
            n = int(input())
            data = list(map(int, input().split()))
        except ValueError:
            print("Invalid input format.")
            return
    else:
        print("Invalid input type.")
        return

    assert len(data) == n

    swaps = build_heap(data)

    # Output number of swaps and each swap
    print(len(swaps))
    for i, j in swaps:
        print(i, j)

if __name__ == "__main__":
    main()
