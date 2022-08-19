def factorial(n):
    if n<1:
        return 1
    else:
        return n*factorial(n-1)

if __name__=="__main__":
    num = int(input("Enter number: "))
    fact = factorial(num)
    print(f"The factorial of the number is: {fact}")