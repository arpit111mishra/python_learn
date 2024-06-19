def show(n):
    if(n==0):       #basecase
        return 1
    print(n,end=" ")
    show(n-1)
show(20) 
