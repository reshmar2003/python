list=[8,3,1,4]
length= len(list)
print(length)
for i in range(0,4):
    print(i)
for i in range(length):
    for j in range(0,length-i-1):
        if list[j]>list[j+1]:
            list[j], list[j+1]=list[j+1],list[j]
print(list)