#!/usr/bin/env python
# coding: utf-8

# In[31]:


import pandas as pd
import numpy as np


# In[32]:


df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN',
'londON_StockhOlm',

'Budapest_PaRis', 'Brussels_londOn'],
'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )',
'12. Air France', '"Swiss Air"']})
df


# In[33]:


df["FlightNumber"]


# In[34]:


newindex=np.arange(1,df.From_To.count()+1)
newindex
df.set_index(newindex, inplace = True)
df


# In[35]:


for i in np.arange(1,df.From_To.count()+1):
    if pd.isnull(df.FlightNumber.loc[i]):
        df.loc[i,'FlightNumber']=df.FlightNumber.loc[i-1]+10
df["FlightNumber"] 
df
        


# In[36]:


df["FlightNumber"].astype(int)


# In[37]:


df[['From','To']]= df.From_To.str.split("_", expand= True)
df


# In[38]:


df.From= df.From.str.capitalize()
df.To= df.To.str.capitalize()
df.From_To=df.From_To.str.capitalize()
print(df)


# In[39]:


df


# In[40]:


df.drop("From_To", axis = 1 , inplace= True)


# In[41]:


df


# In[42]:


df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN',
'londON_StockhOlm',

'Budapest_PaRis', 'Brussels_londOn'],
'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )',
'12. Air France', '"Swiss Air"']})
df


# In[49]:


rows=[]
_ = df.apply(lambda row:[rows.append([row['Airline'],row['FlightNumber'],nn,row['From_To']]) for nn in row.RecentDelays],axis = 1)


# In[50]:


rows


# In[56]:


df1 = pd.DataFrame(rows, columns=df.columns)


# In[57]:


df


# In[58]:


df1


# In[59]:


df2 = pd.DataFrame(df["RecentDelays"].values.tolist())


# In[60]:


df2


# In[61]:


df2.shape[1]


# In[ ]:




