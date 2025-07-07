def staircase(n):
    for i in range(1,n+1):
        separaciones = ' ' * (n-i)
        valores = '#' * i
        total = separaciones + valores
        print(total)
staircase(4)