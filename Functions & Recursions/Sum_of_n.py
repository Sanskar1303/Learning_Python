def sum(n):
    if(n<=0):
        return print(f"{n} is not a natural number")
    if(n==1):
        return 1
    return n + sum(n-1)
n = int(input('Enter a number: '))

print(f'sum of {n} is: ', sum(n))