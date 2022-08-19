def fibonacciNum(n):
    if n==1:
        return 1
    elif n==0:
        return 0
    else:
        return fibonacciNum(n-2) + fibonacciNum(n-1)

if __name__=="__main__":
    series = []
    for i in range(0,11):
        series.append(fibonacciNum(i))
    print(series)