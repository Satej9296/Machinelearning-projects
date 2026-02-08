import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("weather_data.csv")
df = df.head(10)

st.title("Weather Data Visualization Dashboard")

st.subheader("Temperature Trend")
plt.figure()
plt.plot(df["Date"], df["Temperature"])
plt.xticks(rotation=45)
st.pyplot(plt)

st.subheader("Humidity Trend")
plt.figure()
sns.lineplot(x="Date", y="Humidity", data=df)
plt.xticks(rotation=45)
st.pyplot(plt)
