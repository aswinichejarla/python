name=str(raw_input())
count=0
for i in name:
    if(i.isdigit()):
        count=count+1
print(count)
