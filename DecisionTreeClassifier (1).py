
# coding: utf-8

# In[137]:


from sklearn.tree import DecisionTreeClassifier


# In[138]:


from sklearn import tree


# In[139]:


from sklearn.metrics import accuracy_score


# In[140]:


from sklearn.model_selection import train_test_split


# In[141]:


import pandas as pd


# In[142]:


import numpy as np


# In[143]:


dataset = pd.read_csv("C:\Users\hp 1\Desktop\ML\Dataset5Features.csv")


# In[144]:


print(dataset.head())


# In[145]:


cols = ['Mean', 'Variance','SumMPA','MaxMPA','PeakDist']


# In[146]:


X = dataset[cols]


# In[147]:


y = dataset.Label


# In[148]:


model = DecisionTreeClassifier(random_state=1)


# In[149]:


X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.3,random_state = 42,stratify=y)


# In[150]:


model.fit(X_train,y_train)


# In[151]:


y_pred = model.predict(X_test)


# In[152]:


print ('Accuracy is- ', accuracy_score(y_test,y_pred)*100)

