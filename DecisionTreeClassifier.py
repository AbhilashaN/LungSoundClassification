
# coding: utf-8

# In[58]:


from sklearn.tree import DecisionTreeClassifier


# In[59]:


from sklearn import tree


# In[60]:


from sklearn.metrics import accuracy_score


# In[61]:


from sklearn.model_selection import train_test_split


# In[62]:


import pandas as pd


# In[63]:


import numpy as np


# In[64]:


dataset = pd.read_csv("C:\Users\hp 1\Desktop\ML\Dataset5Features.csv")


# In[65]:


print(dataset.head())


# In[66]:


cols = ['Mean', 'Variance','SumMPA','MaxMPA','PeakDist']


# In[67]:


X = dataset[cols]


# In[68]:


y = dataset.Label


# In[69]:


model = DecisionTreeClassifier()


# In[70]:


X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.3,random_state = 42,stratify=y)


# In[71]:


model.fit(X_train,y_train)


# In[72]:


y_pred = model.predict(X_test)


# In[73]:


print ('Accuracy is- ', accuracy_score(y_test,y_pred)*100)

