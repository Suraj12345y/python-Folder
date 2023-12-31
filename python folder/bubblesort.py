def bubblesort(a):
    for i in range(len(a)):
        for j in range(len(a)-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    return a
l=[5,1,9,7,3,6]
print(bubblesort(l))