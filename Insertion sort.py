

import time as t


def insertionSort(alist):
    for i in xrange(1,len(alist)):
        key=alist[i]
        j=i-1
        while j>=0 and alist[j]>key:
           # print alist[j],key
            alist[j+1]=alist[j]
            j=j-1
        alist[j+1]=key
    #print alist

def bubbleSort(lista):
    for i in xrange(0,len(lista),1):
        #print i
        for j in xrange(len(lista)-1,i,-1):
            #print lista[j-1],lista[j]
            if lista[j-1]>lista[j]:
                temp=lista[j-1]
                lista[j-1]=lista[j]
                lista[j]=temp
    #print lista
for m in ["D","I"]:
    for i in xrange(1,13):
        fl = open("{0}{1}.txt".format(m,i), "r")
        lst = []
        a = 0.0
        b = 0.0
        if m == "R":
            sampling = 11
        else:
            sampling = 2
        for line in fl:
            lst.append(int(line.strip()))
        count=len(lst)
        for j in xrange(1, sampling):
            avg=j
            start = t.time()
            insertionSort(lst)
            end = t.time()
            a=a+(end-start)
            start = t.time()
            bubbleSort(lst)
            end = t.time()
            b = b+(end - start)
        print "{0}{1}".format(m,i),"Insertion",count,a/avg
        print "{0}{1}".format(m,i),"Bubble   ",count,b/avg
        fl.close()







#insertionSort(lst)
#bubbleSort(lst)
#end = t.time()
#print ("insertion sort " + str(end-start) + " seconds")

#start1 = t.time()
#insertionSort(lst)
#bubbleSort(lst)
#end1 = t.time()
#print ("Bubble sort " + str(end1-start1) + " seconds")
#print(lst)
