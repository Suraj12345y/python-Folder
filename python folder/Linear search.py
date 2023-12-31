def linearSearch(num,key):
    for i in range(len(num)):
        if key==num[i]:
            return "found at",i
    return "not found"
num=[2,3,6,2,4,9,7,3,3,6,1,0]
key=5

print(linearSearch(num, key))

