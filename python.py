def fibo(*no_of_term):
    if no_of_term[0] == 1:
        print(0)
    elif no_of_term[0] == 2:
        print(0,1)
    else:
        fiboterm = [0,1]
        for i in range(1, no_of_term[0]):
            fiboterms = fiboterm[i] + fiboterm[i - 1]
            fiboterm.append(fiboterms)
        print(fiboterm)

fibo(6)