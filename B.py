a=input()
for i in range(len(a)):
    for j in range(i,len(a)):
        if a[i]>a[j]:
            strlist=list(a)
            strlist[i],strlist[j]=strlist[j],strlist[i]
            a="".join(strlist)
print(a)