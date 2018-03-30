#!/usr/bin/python3
#-*-conding=utf-8 -*-
import subprocess
f=open('kill','w',encoding='utf8')
subprocess.call(['ps','aux'],stdout=f)
f.close()
f=open('kill','r',encoding='utf8')
l=[]
data=f.readlines()
l=data
lis=[]
for i in range(1,len(l)):
    b=l[i].split(' ')
    for j in b:
        if j!='':
            lis.append(j)
lie=[]
for x in range(11,len(lis),11):
    lie.append(lis[:x])
for o in range(len(lie)):
    if lie[o][7]=='z':
        subprocess.call(['kill','-9',lie[o][1]])
