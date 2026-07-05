def fibonnaci(*no_of_terms):
    if no_of_terms[0] == 1:
        print(0)
    elif no_of_terms[0] == 2:
        print(0,1)
    else:
        x = [0,1]
        for i in range(1, no_of_terms[0]):
            if i == no_of_terms[0] - 1:
                break
            fiboterms = x[i] + x[i - 1] # 1 + 0 = 1, 1+1=2, 2+1=3
            x.append(fiboterms)
        print(x)
fibonnaci(5)