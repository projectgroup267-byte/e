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
    df = pd.read_csv("social_media_engagement_enhanced (1).csv")
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
# ----------------------------
# Content Performance - Idea 2
# Engagement Components Comparison
# ----------------------------
st.title("📊 Content Performance: Likes, Comments & Shares")

# Group by content type
content_metrics = (
    df.groupby("content_type")[["likes", "comments", "shares"]]
    .mean()
    .reset_index()
)

# Display table
st.subheader("📌 Average Engagement Metrics by Content Type")
st.dataframe(content_metrics)

# Bar chart for comparison
st.subheader("📊 Content Type vs Engagement Metrics")
st.bar_chart(
    data=content_metrics,
    x="content_type"
)
