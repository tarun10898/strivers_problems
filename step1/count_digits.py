#Count digits in a number


def solve():
    n =list(input("enter the number: "))
    count = 0
    for i in n:
        count += 1
    return count    

if __name__ == "__main__":
    print(solve())
