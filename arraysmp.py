import array
ary1 = array.array("i", [7,8,9])
print ("Array items are: " ,ary1)
ary2= array.array("i", [1,2,6])
n1= len(ary1)
n2=len(ary2)
def mergedarray (ary1,ary2, n1,n2):
    ary3 = [None] * (n1 + n2)
    i=0
    j=0
    k=0
    while i < n1 and j < n2:
        if ary1[i] < ary2[j]:
            ary3[k] = ary1[i]
            k = k+1
            i = i+1
        else:
            ary3[k] = ary2[j]
            k = k+1
            j = j+1  
            while i < n1:
                ary3[k] = ary1[i];
                k = k + 1
                i = i + 1
            while j < n2:
                ary3[k] = ary2[j];
                k = k + 1
                j = j + 1
                for i in range(n1 + n2):
                    print(str(ary3[i]))