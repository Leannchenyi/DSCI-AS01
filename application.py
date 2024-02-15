import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import streamlit as st

# create headers
st.title('Ebay Laptops & Netbooks Sales')
st.markdown('Dataset Application')

# Load dataset
df = pd.read_csv('EbayPcLaptopsAndNetbooksClean.csv')

fig, ax = plt.subplots()

# Histogram
#plt.figure(figsize=(10, 8))
ax = sns.histplot(df['Price'], bins = 20, kde=True)
plt.xlabel('Price $')
plt.ylabel('Frequency')
plt.title('Histogram of Price')
st.pyplot(fig)

# Boxplot of Price by Condition
plt.figure(figsize=(10, 8))
sns.boxplot(x='Condition', y='Price', data=df)
plt.xlabel('Condition')
plt.ylabel('Price ($)')
plt.title('Boxplot of Price by Condition')
st.pyplot()

# Barchart Average Price by Brand
avg_price_by_brand = df.groupby('Brand')['Price'].mean().reset_index()
plt.figure(figsize=(12, 6))
sns.barplot(x='Brand', y='Price', data=avg_price_by_brand)
plt.xlabel('Brand')
plt.ylabel('Average Price ($)')
plt.title('Average Price by Brand')
plt.xticks(rotation=45, ha='right')
st.pyplot()

#Countplot of Condition
plt.figure(figsize=(8, 6))
sns.countplot(x='Condition', data=df)
plt.xlabel('Condition')
plt.ylabel('Count')
plt.title('Countplot of Condition')
plt.xticks(rotation=45, ha='right')
st.pyplot()