#!/usr/bin/env python
# coding: utf-8

# In[105]:


import pandas as pd


# In[106]:


#プレートリーダーで取り込んだデータをソートする（12行 -> 8列）スクリプト。入力と出力のファイル名は自分で指定。

df = pd.read_csv('050209.col',sep='\t',skiprows=(0,1,2),header=(0)) #.col 形式ファイルの取り込み（最初の3行をスキップ）。.csvなら sep=は必要ない。

df.head()


# In[107]:


#index行を取り出し、8列サンプルの順番に置き換え、ソートした後にindexを置き換える。

df_index = (df.index.tolist()) 

new_index = (df.index//12 +1) + (df.index%12)*8

df.insert(0, 'well', new_index)

df_sorted = df.sort_values("well")

df_sorted2 = df_sorted.set_index("well")


# In[108]:


#columnをリセットする。

sh = df_sorted2.shape

df_sorted2.columns = range(sh[1])

df_sorted2.head()


# In[109]:


df_sorted2.to_csv("050209.csv")


# In[ ]:




