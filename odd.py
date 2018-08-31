lower,upper = map(int,raw_input().split())
for n in range(lower,upper+1):
    if(n%2!=0) and n!=1:
        print(n),
