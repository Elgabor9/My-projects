'''
my code takes all lists and each element in each list is a squared
then i make a nested loops and calculte the sum of this nested loops then maximize it as possible and put it in ans which is the max between ans%m and sum%m
so the ans is the max possible sum%m
'''
import math
line = input().split()
k = int(line[0])
m = int(line[1])
ans=0
sum=0
# here i'm taking first list length and elements
line = input().split()
len1=int(line[0])
list1=[]
for i in range(1,len1+1):
    element=int(line[i])
    element*=element
    list1.append(element)
if k>=2: #here i'm checking if k is greater than 2 and taking the rest of lists
    line = input().split()
    len2 = int(line[0])
    list2=[]
    for i in range(1,len2+1):
        element=int(line[i])
        element*=element
        list2.append(element)
    if k>=3:
        line = input().split()
        len3 = int(line[0])
        list3=[]
        for i in range(1,len3+1):
            element=int(line[i])
            element*=element
            list3.append(element)
        if k>=4:
            line = input().split()
            len4 = int(line[0])
            list4=[]
            for i in range(1,len4+1):
                element=int(line[i])
                element*=element
                list4.append(element)
            if k>=5:
                line = input().split()
                len5 = int(line[0])
                list5=[]
                for i in range(1,len5+1):
                    element=int(line[i])
                    element*=element
                    list5.append(element)
                if k>=6:
                    line = input().split()
                    len6 = int(line[0])
                    list6=[]
                    for i in range(1,len6+1):
                        element=int(line[i])
                        element*=element
                        list6.append(element)
                    if k==7:
                        line = input().split()
                        len7 = int(line[0])
                        list7=[]
                        for i in range(1,len7+1):
                            element=int(line[i])
                            element*=element
                            list7.append(element)
for i in range(len(list1)): # here i'm looping through all elements in first list and add them to sum
    sum=list1[i]
    if k>=2: # here i'm checking if k is greater than 2 and taking the rest of lists and add them to sum too
        for j in range(len(list2)):
            sum=list1[i]+list2[j]
            if k>=3:
                for x in range(len(list3)):
                    sum=list1[i]+list2[j]+list3[x]
                    if k>=4:
                        for l in range(len(list4)):
                            sum=list1[i]+list2[j]+list3[x]+list4[l]
                            if k>=5:
                                for z in range(len(list5)):
                                    sum=list1[i]+list2[j]+list3[x]+list4[l]+list5[z]
                                    if k>=6:
                                        for n in range(len(list6)):
                                            sum=list1[i]+list2[j]+list3[x]+list4[l]+list5[z]+list6[n]
                                            if k==7:
                                                for o in range(len(list7)):
                                                    sum=list1[i]+list2[j]+list3[x]+list4[l]+list5[z]+list6[n]+list7[o]
                                                    ans=max(ans%m,sum%m)
                                            else:
                                                ans=max(ans%m,sum%m)
                                    else:
                                        ans=max(ans%m,sum%m)
                            else:
                                ans=max(ans%m,sum%m)
                    else:
                        ans=max(ans%m,sum%m)
            else:
                ans=max(ans%m,sum%m)
    else:
        ans=max(ans%m,sum%m)
print(ans)
