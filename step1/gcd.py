def solve(n1,n2):
    gcd = 1
    for i in range(1,min(n1,n2)+1):
        if n1%i == 0 and n2 % i == 0:
            gcd =i
    return gcd


if __name__ == "__main__":
    n1,n2 = 20,40
    print(solve(n1,n2))

# def find_gcd(a,b):
#     while a>0 and b>0:




# if __name__ == "__main__":
#     n1 = 20 
#     n2 = 40
#     gcd = find_gcd(n1,n2)
#     print(gcd)