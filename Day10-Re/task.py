##Return even if it a even or else odd
def evenodd(n):
    if n%2==0:
        print("even")
    else:
        print("odd")
## prefect number
def isperfect(n):
    f=0
    for i in range(1,n):
        if n%i==0:
            print(i)
            f+=i
    if f==n:
        return "isperfect"
    else:
        return "notperfect"
#isperfect(6)       

   
    