#!/usr/bin/env python
# coding: utf-8

# In[29]:


print("Enter the list: ")
l=list(map(int,input().split(" ")))
for i in l:
    if(i<0):
        l.remove(i)
print(l)

