import streamlit as st
import pandas as pd

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="Social Media Engagement Analytics",
    layout="wide"
)

# ----------------------------
# Title
# ----------------------------
st.title("📊 Engagement Rate Analysis")

# ----------------------------
# Load Dataset
# ----------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("social_media_engagement_enhanced (1)")
    return df

df = load_data()

# ----------------------------
# Engagement Rate Calculation
# ----------------------------
df["total_engagement"] = df["likes"] + df["comments"] + df["shares"]
df["engagement_rate"] = (df["total_engagement"] / df["reach"]) * 100

# ----------------------------
# Platform-wise Engagement Rate
# ----------------------------
platform_engagement = (
    df.groupby("platform")["engagement_rate"]
    .mean()
    .reset_index()
)

# ----------------------------
# Display Table
# ----------------------------
st.subheader("📌 Platform-wise Average Engagement Rate (%)")
st.dataframe(platform_engagement)

# ----------------------------
# Bar Chart (Streamlit Native)
# ----------------------------
st.subheader("📊 Engagement Rate Comparison by Platform")
st.bar_chart(
    data=platform_engagement,
    x="platform",
    y="engagement_rate"
)
