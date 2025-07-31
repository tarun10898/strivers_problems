def solve():
    n = int(input("enter the number"))
    dup = n
    rev = 0
    while n > 0 :
        rem = n % 10
        rev = (rev * 10) + rem
        n = n // 10

    if rev == dup :
        print("it's palindrome")
    else:
        print("it's not palindrome")    
if __name__ == "__main__":
    solve()