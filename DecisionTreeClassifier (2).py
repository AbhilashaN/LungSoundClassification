
# coding: utf-8

# In[79]:


from sklearn.tree import DecisionTreeClassifier


# In[80]:


from sklearn import tree


# In[81]:


from sklearn import preprocessing


# In[82]:


from sklearn.metrics import accuracy_score


# In[83]:


from sklearn.model_selection import train_test_split


# In[84]:


import pandas as pd


# In[85]:


import numpy as np


# In[86]:


dataset = pd.read_csv("C:\Users\hp 1\Desktop\DATASET.csv")


# In[87]:


print(dataset.head())


# In[88]:


cols = ['Mean','Variance','SumMPA','MaxMPA','Fmax']


# In[89]:


X = dataset[cols]


# In[90]:


y = dataset.Label


# In[91]:


print(X.head())


# In[98]:


scaler = preprocessing.StandardScaler()


# In[99]:


scaler = preprocessing.StandardScaler().fit(X_train)


# In[100]:


scaler.transform(X_train)


# In[101]:


scaler.transform(X_test)


# In[286]:


model = DecisionTreeClassifier(random_state=21)


# In[287]:


print(y.head())


# In[288]:


X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.35,random_state = 80,stratify=y)


# In[289]:


model.fit(X_train,y_train)


# In[290]:


y_pred = model.predict(X_test)


# In[291]:


print ('Accuracy is- ', accuracy_score(y_test,y_pred)*100)

