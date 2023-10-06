#!/usr/bin/env python
# coding: utf-8

# In[1]:


import io
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('cd', '"D:\\Imarticus\\stat\\veh"')


# In[2]:


vehicle=pd.read_csv('in-vehicle-coupon-recommendation.csv')
vehicle.head()


# In[3]:


vehicle.info()


# In[4]:


vehicle.describe()


# In[5]:


vehicle.isnull().sum()


# In[6]:


vehicle.car.value_counts(dropna=False)


# In[7]:


vehicle=vehicle.drop(['car','toCoupon_GEQ5min'],axis=1)


# vehicle.car=vehicle.car.fillna('Missing')

# In[8]:


vehicle.Bar.value_counts(dropna=False)


# In[9]:


vehicle.Bar=vehicle.Bar.fillna('never')


# In[10]:


vehicle.CoffeeHouse.value_counts(dropna=False)


# In[11]:


vehicle.CoffeeHouse=vehicle.CoffeeHouse.fillna('less1')


# In[12]:


vehicle.CarryAway.value_counts(dropna=False)


# In[13]:


vehicle.CarryAway=vehicle.CarryAway.fillna('1~3')


# In[14]:


vehicle.Restaurant20To50.value_counts(dropna=False)


# In[15]:


vehicle.Restaurant20To50=vehicle.Restaurant20To50.fillna('less1')


# In[16]:


vehicle.RestaurantLessThan20.value_counts(dropna=False)


# In[17]:


vehicle.RestaurantLessThan20=vehicle.RestaurantLessThan20.fillna('1~3')


# In[18]:


vehicle.isnull().sum()


# In[19]:


vehicle.Y.value_counts()


# In[20]:


vehicle.temperature.value_counts()


# In[21]:


vehicle.has_children.value_counts()


# vehicle.toCoupon_GEQ5min.value_counts()

# In[22]:


vehicle.toCoupon_GEQ15min.value_counts()


# In[23]:


vehicle.toCoupon_GEQ25min.value_counts()


# In[24]:


vehicle.direction_same.value_counts()


# In[25]:


vehicle.direction_opp.value_counts()


# In[26]:


vehicle.temperature=vehicle.temperature.astype('object')
vehicle.has_children=vehicle.has_children.astype('object')
# vehicle.toCoupon_GEQ5min=vehicle.toCoupon_GEQ5min.astype('object')
vehicle.toCoupon_GEQ15min=vehicle.toCoupon_GEQ15min.astype('object')
vehicle.toCoupon_GEQ25min=vehicle.toCoupon_GEQ25min.astype('object')
vehicle.direction_same=vehicle.direction_same.astype('object')
vehicle.direction_opp=vehicle.direction_opp.astype('object')


# In[27]:


vehicle.info()


# # EDA

# In[28]:


vehicle.temperature.value_counts().plot(kind='pie',autopct='%0.2f%%')


# In[29]:


ax=vehicle.coupon.value_counts().plot(kind='bar')
for i in ax.containers:
    ax.bar_label(i)


# In[30]:


vehicle.Bar.value_counts().plot(kind='pie',autopct='%0.2f%%')


# In[31]:


vehicle.age.value_counts().plot()


# In[32]:


ax=vehicle.education.value_counts().plot(kind='bar')
for i in ax.containers:
    ax.bar_label(i)


# In[33]:


pd.crosstab(vehicle.gender,vehicle.education).plot(kind='bar')


# In[34]:


ax=pd.crosstab(vehicle.time,vehicle.expiration).plot(kind='bar')
for i in ax.containers:
    ax.bar_label(i)


# # Hypothesis testing

# In[35]:


pd.crosstab(vehicle.gender,vehicle.education)


# In[36]:


pd.crosstab(vehicle.time,vehicle.expiration)


# In[37]:


pd.crosstab(vehicle.coupon,vehicle.expiration)


# In[38]:


from scipy.stats import chi2_contingency


# In[39]:


chi2_contingency(pd.crosstab(vehicle.coupon,vehicle.time))
# since pvalue=1.4958878106088764e-224 is leassthan 0.05, reject null hypothesis


# In[40]:


chi2_contingency(pd.crosstab(vehicle.coupon,vehicle.expiration))
# since pvalue=5.450753447977153e-153 is lessthan 0.05, reject null hypothesis


# In[41]:


chi2_contingency(pd.crosstab(vehicle.gender,vehicle.education))
# since pvalue=0.00038255454739335337 is lessthan 0.05, reject null hypothesis


# In[42]:


chi2_contingency(pd.crosstab(vehicle.gender,vehicle.occupation))
# since pvalue=0.0 is lessthan 0.05, reject null hypothesis


# In[43]:


chi2_contingency(pd.crosstab(vehicle.coupon,vehicle.occupation))
# since pvalue=0.9999894480826622 is greater than 0.05, fail to reject null hypothesis


# In[44]:


ax=vehicle.Y.value_counts().plot(kind='bar')
for i in ax.containers:
    ax.bar_label(i)


# In[ ]:





# # preprocessing

# In[45]:


vehicle


# In[46]:


vehicle.columns


# In[47]:


numcols=vehicle.select_dtypes(include=np.number)
objcols=vehicle.select_dtypes(include='object')


# In[48]:


objcols.head()


# In[49]:


from sklearn.preprocessing import LabelEncoder


# In[50]:


objcols=objcols.astype(str).apply(LabelEncoder().fit_transform)


# In[51]:


numcols.head()


# In[52]:


combine_df=pd.concat([numcols,objcols],axis=1)


# In[53]:


combine_df.head()


# In[54]:


combine_df.replace({True:1,False:0},inplace=True)


# In[55]:


combine_df.head()


# In[56]:


y=combine_df.Y
X=combine_df.drop('Y',axis=1)


X.head()
from sklearn.ensemble import GradientBoostingClassifier



gbc=GradientBoostingClassifier(n_estimators=1000,max_depth=4)




gbcmodel=gbc.fit(X,y)



gbcmodel.score(X,y)



gbcpredict=gbcmodel.predict(X)



import pickle

pickle.dump(gbc,open('gbmmodel.pkl','wb'))#wb- meanas write

pickle_model=pickle.load(open('gbmmodel.pkl','rb'))# rb - means read


