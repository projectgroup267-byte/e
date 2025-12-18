import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page config
st.set_page_config(page_title="Engagement Rate Analysis", layout="wide")

# Title
st.title("📊 Social Media Engagement Rate Analysis")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("social_media_engagement.csv")
    return df

df = load_data()

# Engagement calculation
df["total_engagement"] = df["likes"] + df["comments"] + df["shares"]
df["engagement_rate"] = (df["total_engagement"] / df["reach"]) * 100

# Platform-wise aggregation
platform_engagement = df.groupby("platform")["engagement_rate"].mean()

# Display data
st.subheader("📌 Platform-wise Engagement Rate (%)")
st.dataframe(platform_engagement.reset_index())

# Plot
fig, ax = plt.subplots()
platform_engagement.plot(kind="bar", ax=ax)
ax.set_xlabel("Platform")
ax.set_ylabel("Engagement Rate (%)")
ax.set_title("Average Engagement Rate by Platform")

st.pyplot(fig)
