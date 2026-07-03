def fibo(*n):
    if n[0] == 1:
        print(0)
    elif n[0] == 2:
        print(0,1)
    else:
        fiboterm = [0,1]
        for i in range(1, n[0]):
            if i == n[0] - 1:
                break
            fiboterms = fiboterm[i] + fiboterm[i - 1]
            fiboterm.append(fiboterms)
        for x in fiboterm:
            print(x)

fibo(5)