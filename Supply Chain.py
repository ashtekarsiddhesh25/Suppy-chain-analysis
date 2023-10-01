#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Importing Libraries
import pandas as pd
import plotly.express as px #to create entire fig of data at once
import plotly.io as pio     #a free and open-source graphing library for Python
import plotly.graph_objects as go 
pio.templates.default = "plotly_white"


# In[2]:


data = pd.read_csv("supply_chain_data.csv")
print(data.head())


# In[3]:


print(data.describe())


# In[4]:


fig = px.scatter(data, x='Price', 
                 y='Revenue generated', 
                 color='Product type', 
                 hover_data=['Number of products sold'], 
                 trendline="ols")


# In[5]:


# Sales
sales_data = data.groupby('Product type')['Number of products sold'].sum().reset_index()

pie_chart = px.pie(sales_data, values='Number of products sold', names='Product type', 
                   title='Sales by Product Type', 
                   hole=0.5,
                   color_discrete_sequence=px.colors.qualitative.Alphabet)
                   
pie_chart.update_traces(textposition='inside', textinfo='percent+label')
pie_chart.show()


# In[6]:


sales_data = data.groupby('Product type')['Number of products sold'].sum().reset_index()

pie_chart = px.pie(sales_data, values='Number of products sold', names='Product type', 
                   title='Sales by Product Type', 
                   hole=0.5,
                   color_discrete_sequence=px.colors.qualitative.Alphabet)
                   
pie_chart.update_traces(textposition='inside', textinfo='percent+label')
pie_chart.show()


# In[7]:


total_revenue = data.groupby('Shipping carriers')['Revenue generated'].sum().reset_index()
fig = go.Figure()
fig.add_trace(go.Bar(x=total_revenue['Shipping carriers'], 
                     y=total_revenue['Revenue generated']))
fig.update_layout(title='Total Revenue by Shipping Carrier', 
                  xaxis_title='Shipping Carrier', 
                  yaxis_title='Revenue Generated')
fig.show()


# In[8]:


avg_lead_time = data.groupby('Product type')['Lead time'].mean().reset_index()
avg_manufacturing_costs = data.groupby('Product type')['Manufacturing costs'].mean().reset_index()
result = pd.merge(avg_lead_time, avg_manufacturing_costs, on='Product type')
result.rename(columns={'Lead time': 'Average Lead Time', 'Manufacturing costs': 'Average Manufacturing Costs'}, inplace=True)
print(result)


# In[9]:


revenue_chart = px.line(data, x='SKU', # Stock Keeping Units
                        y='Revenue generated', 
                        title='Revenue Generated by SKU')
revenue_chart.show()


# In[10]:


stock_chart = px.line(data, x='SKU', 
                      y='Stock levels', 
                      title='Stock Levels by SKU')
stock_chart.show()


# In[11]:


order_quantity_chart = px.bar(data, x='SKU', 
                              y='Order quantities', 
                              title='Order Quantity by SKU')
order_quantity_chart.show()


# # Cost Analysis

# In[12]:


shipping_cost_chart = px.bar(data, x='Shipping carriers', 
                             y='Shipping costs', 
                             title='Shipping Costs by Carrier')
shipping_cost_chart.show()


# In[13]:


# Transportation Mode Cost
transportation_chart = px.pie(data, 
                              values='Costs', 
                              names='Transportation modes', 
                              title='Cost Distribution by Transportation Mode',
                              hole=0.5,
                              color_discrete_sequence=px.colors.qualitative.Pastel)
transportation_chart.show()


# In[14]:


# Analysing Defect Rate 
defect_rates_by_product = data.groupby('Product type')['Defect rates'].mean().reset_index()

fig = px.bar(defect_rates_by_product, x='Product type', y='Defect rates',
             title='Average Defect Rates by Product Type')
fig.show()


# In[15]:


# An important part of data analysis is the process of grouping, summarizing, aggregating and calculating statistics about this data. Pandas pivot tables provide a powerful tool to perform these analysis techniques with Python.


# In[16]:


pivot_table = pd.pivot_table(data, values='Defect rates', 
                             index=['Transportation modes'], 
                             aggfunc='mean')

transportation_chart = px.pie(values=pivot_table["Defect rates"], 
                              names=pivot_table.index, 
                              title='Defect Rates by Transportation Mode',
                              hole=0.5,
                              color_discrete_sequence=px.colors.qualitative.Pastel)
transportation_chart.show()


# In[17]:


stock_chart = px.line(data, x='SKU', 
                      y='Stock levels', 
                      title='Stock Levels by SKU')
stock_chart.show()


# In[18]:


import matplotlib.pyplot as plt
import numpy as np
classes = ["Python", "R", "AI", "ML", "DS"]
class1_students = [30, 10, 20, 25, 10]


plt.bar(classes,class1_students,width=0.3,align='edge',color='y',edgecolor='r',label='class 1')

plt.title('Student',fontsize=20)
plt.xlabel('Classes',fontsize=15)
plt.ylabel("Classes 1",fontsize=15)

plt.legend()
plt.show()


# In[19]:


sku = ['SKU0','SKU1','SKU2','SKU3','SKU4','SKU5']
Stock_levels = [58,53,1,23,5,90]

plt.bar(sku,Stock_levels, width=0.3, align='edge' , color = 'blue' , edgecolor = "red" , label = 'classes 1')
plt.title = ("Supply Chain")
plt.xlabel = ('hel')
plt.ylabel = ('Stock_levels')
plt.legend()
plt.show()

