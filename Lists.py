# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 21:10:57 2021

@author: geoto
"""
    







#clear list
item=mylist3.clear()
print(item)
print('-----------------------------------------------')
#reverse list
print(mylist)
list_rev=mylist.reverse()#reverse() used inplace=True so the change takes immediate effect on mylist
print(mylist)
listaa=[19,5,34,74,2,43]
print(listaa)
xxx=listaa.sort() #sort() used inplace=True so the change takes immediate effect on the listaa
#sort list
print(listaa)

#to avoid that we can use the sorted() method as inplace=false in this case
a_list=[1,5,9,3,8,4]
print(sorted(a_list))
print(a_list)

# create list with zeros
zero_list=[0]*3
print(zero_list)

# adding lists
f_list=[1,2,3,4,5]
s_list=[6,7,8,9,10]
n_list=f_list+s_list
print(n_list)

# new list part of original list
o_list=[1,2,3,4,5,6,7,8,9,10]
n_list=o_list[3:7]
#returns 4,5,6,7 (indices,3,4,5,6)
print(n_list)

lstrev=o_list[::-1]#returns list elements in reverse order
lst2=o_list[::2]# returns list elements of step 2
print(lstrev)
print(lst2)

# if list b = list a, then changes will be applied to both lists
list_a=[1,2,3,4,5]
list_b=list_a
list_b.insert(0,0)
print(list_a)
print(list_b)
print('\r')
#with copy
list_a=[1,2,3,4,5]
list_b=list_a.copy()
list_b.insert(0,0)
print(list_a)
print(list_b)

#with list
list_a=[1,2,3,4,5]
list_b=list(list_a)
list_b.insert(0,0)
print(list_a)
print(list_b)
# with slices
#with copy
list_a=[1,2,3,4,5]
list_b=list_a[:]
list_b.insert(0,0)
print(list_a)
print(list_b)

# calculation within lists
first_list=[1,2,3,4,5]
second_list=[x*x*x for x in first_list]
print(second_list)