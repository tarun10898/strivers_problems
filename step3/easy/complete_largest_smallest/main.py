def  smallest_2nd_smallest(arr,n):
    small = float('inf')
    second_smallest = float('inf')
    for i in range(n):
        if (arr[i]< small):
            second_smallest = small
            small = arr[i]
        elif (arr[i]<second_smallest and arr[i] != small):
            second_smallest = arr[i]    
    return(small,second_smallest)        

def largest_2nd_largest(arr,n):
    large = float('-inf')
    second_largest = float('-inf')
    for i in range(n):
        if (arr[i] > large):
            second_largest = large
            large = arr[i]
        elif (arr[i]>second_largest and arr[i] != large):
            second_largest = arr[i]
    return (large,second_largest)            


if __name__ == "__main__":
    n=int(input("enter the count of the array elemts to be added"))
    arr = list(map(int,input("enter the elements of the array").strip().split()))[:n]
    print(largest_2nd_largest(arr,n))
    print(smallest_2nd_smallest(arr,n))


