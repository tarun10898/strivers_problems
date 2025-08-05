def solve(arr, n):
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

if __name__ == "__main__":
    n = int(input("Enter the number of elements in the array: "))
    arr = list(map(int, input("Enter the elements of the array separated by space: ").strip().split()))
    if solve(arr, n):
        print("The array is sorted in non-decreasing order.")
    else:
        print("The array is not sorted.")
