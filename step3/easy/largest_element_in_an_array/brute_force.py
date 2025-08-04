# Problem Statement: Given an array, we have to find the largest element in the array.

# Examples

# Example 1:
# Input: arr[] = {2,5,1,3,0};
# Output: 5
# Explanation: 5 is the largest element in the array. 

# Example2: 
# Input: arr[] = {8,10,5,7,9};
# Output: 10
# Explanation: 10 is the largest element in the array. 

def solve():
    n=int(input("enter the count of the values: "))
    arr = list(map(int,input("enter the values in the array: ").strip().split()))
    sorted_arr = sorted(arr)
    largest_arr = sorted_arr[-1]
    print(largest_arr)
if __name__ == "__main__":
    solve()