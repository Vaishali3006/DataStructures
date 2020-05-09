#!/usr/bin/env python
# coding: utf-8

# In[1]:


#list
l1=[1,2,3,4,5,6]
for i in l1:
    print(i)
    


# In[2]:


#printing particular element from list
print(l1[1])


# In[3]:


#list can contain element of different data types
l2=[1,2.0,"Hello",[4,5,6]]
for i in l2:
    print(i)


# In[4]:


#accessing particular range
print(l1[2:5])


# In[5]:


#nested indexing
l3=[[1,3,5],['Hi','Hello'],[2,4,6]]
#to print hi
print(l3[1][1])
#to print 6
print(l3[2][2])


# In[6]:


#negative indexing
l4=['c','o','m','p','u','t','e','r']
#indexing start from right to left with -1 as begining
print(l4[-1])


# In[7]:


#to print "mpute"
print(l4[-6:-1])


# In[8]:


#to add an element in the list-appl1
l1.append(9)
print(l1)


# In[9]:


#to add more then one element in the list
l1.extend([11,13,150])
print(l1)


# In[1]:


#tuple
t1=(1,2,3,4)
print(t1)


# In[2]:


#length of tuple
print(len(t1))


# In[3]:


#display any element
print(t1[2])


# In[4]:


#set
set1={1,2,3,4,5,6,7,8}
print(set1)


# In[6]:


#adding element to set
set1.add(10)
print(set1)


# In[7]:


#deleting element from set
set1.remove(2)
print(set1)


# In[8]:


print(len(set1))


# In[9]:


#to print a particular element from a set we have to use looping and ifelse as there is no indexing
for i in set1:
    if i==3:
        print(i)


# In[10]:


#dictionary
dict1={101:"Tanu",102:"Aman"}
print(dict1)


# In[11]:


#length of dictionary
print(len(dict1))


# In[12]:


#print particular element
print(dict1[101])


# In[13]:


#printing any element using get()
dict1.get(102)


# In[14]:


#adding new pair in dictionary
dict1[103]="Gourav"
print(dict1)


# In[15]:


#deleting a pair
del dict1[102]
print(dict1)


# In[16]:


#changing value
dict1[101]="Aman"


# In[17]:


print(dict1)


# In[22]:


#deleting element
dict1.pop(101)
dict1.popitem()


# In[23]:


#all pairs deleted but dictionary will remain
dict1.clear()


# In[24]:


print(dict1)


# In[25]:


dict1[101]="hi"
print(dict1)


# In[26]:


#delete dictionary completely
del dict1


# In[27]:


print(dict1)

