def solve():
    n=int(input("enter the number: "))
    m =len(str(n))
    sum = 0
    dup = n
    while n>0:
        rem = n % 10
        sum = sum + rem ** m
        n = n // 10

    print(sum)  
    if dup == sum:
        print("yes")
    else:
        print("no")

if __name__ == "__main__":
    solve()
