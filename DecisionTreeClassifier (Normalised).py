
# coding: utf-8

# In[166]:


from sklearn.tree import DecisionTreeClassifier


# In[167]:


from sklearn import tree


# In[168]:


from sklearn import preprocessing


# In[169]:


from sklearn.metrics import accuracy_score


# In[170]:


from sklearn.model_selection import train_test_split


# In[171]:


import pandas as pd


# In[172]:


import numpy as np


# In[173]:


dataset = pd.read_csv("C:\Users\hp 1\Desktop\ML\Dataset5Features.csv")


# In[174]:


print(dataset.head())


# In[175]:


cols = ['Mean', 'Variance','SumMPA','MaxMPA','PeakDist']


# In[176]:


X = dataset[cols]


# In[177]:


y = dataset.Label


# In[178]:


model = DecisionTreeClassifier(random_state=1)


# In[179]:


X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.3,random_state = 42,stratify=y)


# In[180]:


scaler = preprocessing.StandardScaler()


# In[181]:


scaler = preprocessing.StandardScaler().fit(X_train)


# In[182]:


scaler.transform(X_train)


# In[183]:


scaler.transform(X_test)


# In[184]:


model.fit(X_train,y_train)


# In[185]:


y_pred = model.predict(X_test)


# In[186]:


print ('Accuracy is- ', accuracy_score(y_test,y_pred)*100)

