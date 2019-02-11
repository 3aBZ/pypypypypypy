# -*- coding: utf-8 -*-
list1=[]
while True:
    couse=input()
    if couse=='0':
        break
    list1.append(couse)
    
for i in range(len(list1)):
    print(str(i+1)+'.'+list1[i])
