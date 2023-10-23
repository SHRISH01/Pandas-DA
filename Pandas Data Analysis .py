#!/usr/bin/env python
# coding: utf-8

# In[37]:


import pandas as pd


# In[38]:


df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')


# In[39]:


type(df)


# In[40]:


df.head(2)


# In[41]:


df.dtypes


# In[42]:


df.tail(4)

# last items


# In[43]:


df.info()


# In[44]:


# As there are less no. of records in Age , Cabin and Embarked , we have to handle these null values to proceed further :


# In[45]:


df.describe()


# In[46]:


df.columns


# In[47]:


df.dtypes == 'object'


# In[48]:


col  = df.dtypes[df.dtypes == 'object'].index


# In[49]:


col


# In[50]:


df[col].describe()


# In[51]:


"""
Difference between a liust and a sereies is only that list doesn't provide us the indices.....
A Pandas series requires all data elements to be of the same data type,
while a Python list can contain elements of different data types. 

"""
#__e.g.__


# In[52]:


l = [1,2,3,4,5,6,4]


# In[53]:


l[0]


# In[54]:


l[l==4]


# Adding a new column in the dataset :

# In[ ]:





# In[55]:


df


# In[56]:


df['Name']


# In[57]:


df['Name'][0:15:2]


# In[58]:


df['Age'].isnull() == True


# In[59]:


df[df['Age'].isnull() == True]


# In[60]:


df[df['Age'].isnull() == True].index


# In[61]:


len(df[df['Age'].isnull() == True].index)


# In[62]:


# To get all null values of Age Column in a single frame :

# Using the Loc - function --


# In[63]:


ind = df[df['Age'].isnull() == True].index


# In[64]:


df.loc[ind]


# In[65]:


df[df['Age'].isnull() == True]


# In[66]:


# To find the person who paid the max fare for this trip :


# In[67]:


df['Fare']


# In[68]:


max(df['Fare'])


# In[69]:


df[df['Fare'] == max(df['Fare'])]


# In[70]:


df['Age'].isnull() == True


# In[71]:


df[df['Age'].isnull() == True]


# In[72]:


df[df['Age'].isnull() == True].index


# In[73]:


# How many males and females are onboarded ?


# In[75]:


df['Sex'].value_counts()


# In[78]:


len(df[df['Sex']=='male'])


# In[79]:


len(df[df['Sex']=='female'])


# In[81]:


df.groupby('Sex').count()


# In[82]:


# How many survived ?


# In[84]:


# we have two values 1 & 0 , we have to filter the data :


# In[88]:


df['Survived'].value_counts()


# In[90]:


df[df['Survived']==1]


# In[91]:


df


# In[93]:


df['Age']


# In[99]:


for i in range(len('Age')):
    if i > 60 :
        print(df[i])


# In[100]:


df['Age'] > 60


# In[101]:


df[df['Age']>60]


# In[103]:


max(df['Age'])


# In[106]:


df[df['Age']==max(df['Age'])]['Name']


# In[ ]:





# In[ ]:





# In[104]:


# How many Casualities we have ?


# In[98]:


df[df['Survived']==0]


# In[ ]:





# In[ ]:





# In[107]:


# How many passangers do we have in 1st , 2nd and 3rd class :


# In[ ]:





# In[108]:


df['Pclass'].value_counts()


# In[109]:


df.groupby('Pclass').count()


# In[ ]:





# In[110]:


# No. of persons name starts with 'S'?


# In[ ]:





# In[123]:


df[df['Name'].str.startswith('S' , 's')]['Name']


# In[ ]:





# In[124]:


df


# In[ ]:





# In[ ]:





# In[ ]:





# In[126]:


# Creating a summation column of sibsp & parch :


# In[ ]:





# In[130]:


col1 = df['SibSp']


# In[134]:


col2 = df['Parch']


# In[135]:


df['col3'] = col1 = col2


# In[139]:


df['col3']


# In[140]:


df


# In[141]:


# Created


# In[ ]:





# In[142]:


# How many person died below age  of 40 ?


# In[149]:


df[(df['Survived'] == 0) & (df['Age'] < 40)]


# In[ ]:





# In[150]:


# From the cabin column seperate integral and alphabetic values


# In[152]:


df['Cabin'].unique()


# In[ ]:





# In[156]:


import re 


# In[159]:


replace = re.compile("(['A-Za-z']+)")


# In[160]:


df['str_cabin'] = df['Cabin'].str.extract(replace)


# In[161]:


df['num_cabin'] = df['Cabin'].str.replace(replace,"")


# In[162]:


df['num_cabin'] 


# In[163]:


df


# In[ ]:




