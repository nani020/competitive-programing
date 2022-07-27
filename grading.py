x=int(input())
for i in range(x):
    g=int(input())
    if g>=38:
        a=g%5
        if a>=3:
            h=5-a
            g=g+h
            g%5==0
    print(g)            
    
