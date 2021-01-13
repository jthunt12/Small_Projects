#################################################
# File: CompareSorts.py
# Author: Jonathan Troy Hunt
# Date: 3/28/2017
# Email: jthunt92@gmail.com
# Class: CSC 231 Data Structures -- Universtiy of North Carolina Wilmington
# Description:
#
#   Compare the varying speeds of two quicksort methods.
#   The first one using the "Median 3" for its pivot, and the
#   the second using index[1] as its pivot
#
#   Additional sorting methods are listed however keep in mind that they might not be practical
#   for such large data sets.
#
################################################

import random
import time

#Bubble Sort
def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

#Selection Sort
def selectionSort(alist):
   for fillslot in range(len(alist)-1,0,-1):
       positionOfMax=0
       for location in range(1,fillslot+1):
           if alist[location]>alist[positionOfMax]:
               positionOfMax = location

       temp = alist[fillslot]
       alist[fillslot] = alist[positionOfMax]
       alist[positionOfMax] = temp

#Insertion Sort
def insertionSort(alist):
   for index in range(1,len(alist)):
     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue

#Shell Sort
def shellSort(alist):
    sublistcount = len(alist)//2
    while sublistcount > 0:
      for startposition in range(sublistcount):
        gapInsertionSort(alist,startposition,sublistcount)
      sublistcount = sublistcount // 2

def gapInsertionSort(alist, start, gap):
    for i in range(start + gap, len(alist), gap):
        currentvalue = alist[i]
        position = i
        while position >= gap and \
                        alist[position - gap] > currentvalue:
            alist[position] = alist[position - gap]
            position = position - gap
        alist[position] = currentvalue

#Quick Sort
def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)
def quickSortHelper(alist,first,last):
   if first<last:
       splitpoint = partition(alist,first,last)
       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)

def median_value(a, f, l, m):
    if a[f] < a[l]:
        if a[l] < a[m]:
            return l
        else:
            return m
    else:
        if a[f] < a[m]:
            return f
        else:
            return m

def partition(alist,first,last):

   pivotIndex = median_value(alist, first, last, (first + last)//2)
   pivotvalue = alist[pivotIndex]
   alist[first], alist[pivotIndex] = alist[pivotIndex], alist[first]
   leftmark = first+1
   rightmark = last
   done = False
   while not done:
       while leftmark <= rightmark and \
               alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1
       while alist[rightmark] >= pivotvalue and \
               rightmark >= leftmark:
           rightmark = rightmark -1
       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp
   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp
   return rightmark

def quickSort01(alist):
   quickSortHelper01(alist,0,len(alist)-1)

def quickSortHelper01(alist,first,last):
   if first<last:
       splitpoint = partition01(alist,first,last)
       quickSortHelper01(alist,first,splitpoint-1)
       quickSortHelper01(alist,splitpoint+1,last)

def partition01(alist,first,last):
   pivotvalue = alist[first]
   leftmark = first+1
   rightmark = last
   done = False
   while not done:
       while leftmark <= rightmark and \
               alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1
       while alist[rightmark] >= pivotvalue and \
               rightmark >= leftmark:
           rightmark = rightmark -1
       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp
   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp
   return rightmark

#Merge Sort
def mergeSort(alist):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        mergeSort(lefthalf)
        mergeSort(righthalf)
        i=0
        j=0
        k=0
        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i]<righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1
        while i<len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1
        while j<len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1

n = 1
numberOfExperiments = 100
print("N  Quicksort_Median_3, Reg_Quicksort")
r=0
for n in range (100, 10000, 500):
    # sumBubble = 0
    # sumSelect = 0
    # sumInsert = 0
    # sumShell = 0
    # sumMerge = 0
    sumQuick = 0
    sumQuick01 = 0
    for x in range(numberOfExperiments):
        """The first 90% of the list is sorted, the last 10% is in random order"""
        MyList = []
        for i in range (int(0.9*n)):
            r=r+1
            MyList.append(r)
        for i in range (int(0.1*n)):
            r = random.randint(1, 2*n)
            MyList.append(r)
        """
        Random List
        """
        # for i in range (n):
        #     r = random.randint(1, 2*n)
        #     MyList.append(r)
        """
        Create Lists
        """
        # myList2 = MyList[:]
        # myList3 = MyList[:]
        # myList4 = MyList[:]
        # myList5 = MyList[:]
        myList6 = MyList[:]
        myList7 = MyList[:]

        # start = time.clock()
        # bubbleSort(MyList)
        # end = time.clock()
        # sumBubble += (end - start)
        #
        # start = time.clock()
        # selectionSort(myList2)
        # end = time.clock()
        # sumSelect += (end - start)
        #
        # start = time.clock()
        # insertionSort(myList3)
        # end = time.clock()
        # sumInsert += (end - start)
        #
        # start = time.clock()
        # shellSort(myList4)
        # end = time.clock()
        # sumShell += (end - start)
        #
        # start = time.clock()
        # mergeSort(myList5)
        # end = time.clock()
        # sumMerge += (end - start)

        start = time.clock()
        quickSort(myList6)
        end = time.clock()
        sumQuick += (end - start)

        start = time.clock()
        quickSort01(myList7)
        end = time.clock()
        sumQuick01 += (end - start)

    print(n, sumQuick/numberOfExperiments ,' ', sumQuick01/numberOfExperiments)
