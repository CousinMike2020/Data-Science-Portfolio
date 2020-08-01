#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as py

#Import the notebooks we'll be using for our analysis


# In[2]:


ecomm = pd.read_csv('/Users/MikeBurton/Downloads/Refactored_Py_DS_ML_Bootcamp-master 2/04-Pandas-Exercises/Ecommerce Purchases')

#Read in the CSV with our customer data and turn it into a database


# In[ ]:





# In[3]:


ecomm #Calling back our database


# In[8]:


ecomm.info()
#Call back ".info()" to see how many rows and columns there are


# In[10]:


ecomm['Purchase Price'].mean()
#Use the next 3 lines of code to callback specific purchase price information


# In[11]:


ecomm['Purchase Price'].max()


# In[12]:


ecomm['Purchase Price'].min()


# In[13]:


ecomm.head(3)
#Now we want to look at the first three rows of the column


# In[15]:


ecomm[ecomm['Language']=='en']
#We want to now identify how many customers speak English as a primary language


# In[17]:


len(ecomm[ecomm['Job'] =='Lawyer'].index)
#Now we want to know how many customers have "lawyer" in their job field


# In[22]:


ecomm['AM or PM'].value_counts()
#We'd like to determine how many customers make purchases in the daytime vs the nighttime 


# In[24]:


ecomm['Job'].value_counts().head(5)
#Through using this line of code we can see what the 5 most common job titles are in our dataset.


# In[26]:


ecomm[ecomm['Lot']=='90 WT']


# In[27]:


ecomm[ecomm['Credit Card']==4926535242672853]['Email']
#Using a particular customer credit card number to find email associated with that credit card


# In[32]:


ecomm[(ecomm['CC Provider']=='American Express') & (ecomm['Purchase Price']>95)].count()
#We'd like to know how many customers have American Express as their credit card provider and have made purchases greater than $95


# In[36]:


sum(ecomm['CC Exp Date'].apply(lambda exp: exp[3:]=='25'))
#Here we'd like to know how many people have a credit card that expires in 2025.


# In[38]:


ecomm['Email'].apply(lambda email: email.split('@')[1]).value_counts().head(5)
#Here we'd like to see a list of the top email providers


# In[ ]:




