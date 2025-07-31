def solve():
    divisiors = []
    n=int(input("enter the number: "))
    for i in range(1, n+1):
        if (n%i == 0):
            divisiors.append(i)
    return divisiors        
if __name__ == "__main__":
    print(solve())