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

def solve(arr,n):
    lar = arr[0]
    for i in range(1,n):
        if lar<arr[i]:
            lar = arr[i]
    return lar        

if __name__ == "__main__":
    n= int(input("enter the count of the array"))
    arr = list(map(int,input("enter the elements in the array").strip().split()))[:n]
    print(solve(arr,n))