
# coding: utf-8

# In[160]:


from sklearn.model_selection import train_test_split


# In[161]:


from sklearn.metrics import accuracy_score


# In[162]:


import pandas as pd


# In[163]:


import numpy as np


# In[164]:


from sklearn.model_selection import train_test_split


# In[165]:


from sklearn.ensemble import RandomForestClassifier


# In[166]:


dataset = pd.read_csv("C:\Users\hp 1\Desktop\ML\Dataset5Features.csv")


# In[167]:


cols = ['Mean', 'Variance','SumMPA','MaxMPA','PeakDist']


# In[168]:


X = dataset[cols]


# In[169]:


print(X.head())


# In[170]:


y = dataset.Label


# In[201]:


X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.3,random_state=42,stratify=y)


# In[230]:


model = RandomForestClassifier(random_state=55)


# In[231]:


model.fit(X_train,y_train)


# In[232]:


y_pred = model.predict(X_test)


# In[233]:


print ('Accuracy is- ', accuracy_score(y_test,y_pred)*100)

