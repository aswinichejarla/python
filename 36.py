name=raw_input()
count=0
for i in name:
    if(i.isspace()):
        count=count+1
print(count)
