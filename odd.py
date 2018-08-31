lower,upper = map(int,raw_input().split())
for a in range(lower,upper+1):
    if(a%2!=0) and a!=1:
        print(a),
