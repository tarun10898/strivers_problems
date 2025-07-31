def solve():
    n=list(input("enter the number"))
    low = 0
    high = len(n)-1
    while low<high:
        n[low],n[high] = n[high],n[low]
        low += 1
        high -= 1
    return ("".join(n))     


if __name__ == "__main__":
    print(solve())


def solve():
    n = int(input("Enter the number: "))
    rev = 0
    while n > 0:
        rem = n % 10          # Extract last digit
        rev = rev * 10 + rem  # Append it to the reversed number
        n = n // 10           # Remove the last digit
    print(rev)

if __name__ == "__main__":
    solve()
