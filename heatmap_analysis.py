import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from faker import Faker

# 1. 设置页面
st.set_page_config(
    page_title="HelloFresh Reactivation Analyzer",
    page_icon="🍴",
    layout="wide"
)

# 2. 生成假想数据（替换为您的真实数据）
@st.cache_data
def load_data():
    fake = Faker()
    data = []
    for _ in range(200):
        data.append({
            'industry': 'insurance',
            'segment': fake.random_element(['high_risk', 'medium_risk', 'low_risk']),
            'reactivation_rate': fake.random_int(min=15, max=45),
            'channel': fake.random_element(['call', 'email', 'SMS'])
        })
        data.append({
            'industry': 'meal_kit',
            'segment': fake.random_element(['vegan', 'family', 'gourmet']),
            'reactivation_rate': fake.random_int(min=25, max=60),
            'channel': fake.random_element(['app_push', 'email', 'retargeting'])
        })
    return pd.DataFrame(data)

df = load_data()

# 3. 侧边栏控件
st.sidebar.header("Filters")
selected_industry = st.sidebar.multiselect(
    "Industry", 
    options=df['industry'].unique(),
    default=df['industry'].unique()
)

selected_segment = st.sidebar.multiselect(
    "Segment",
    options=df['segment'].unique(),
    default=['vegan', 'high_risk']
)

# 4. 过滤数据
filtered_df = df[
    (df['industry'].isin(selected_industry)) &
    (df['segment'].isin(selected_segment))
]

# 5. 主界面
st.title("📊 From Insurance to Meal Kits: Reactivation Strategy Dashboard")
st.markdown("""
    *Compare performance across industries*  
    *Data source: Generated synthetic data*
""")

# 6. 核心图表
col1, col2 = st.columns(2)

with col1:
    st.subheader("Reactivation Rate by Segment")
    fig1 = plt.figure(figsize=(10, 6))
    sns.barplot(
        data=filtered_df,
        x='segment',
        y='reactivation_rate',
        hue='industry',
        palette=['#1B8D4A', '#FF8000']  # HelloFresh colors
    )
    plt.xticks(rotation=45)
    st.pyplot(fig1)

with col2:
    st.subheader("Channel Effectiveness")
    fig2 = plt.figure(figsize=(10, 6))
    sns.boxplot(
        data=filtered_df,
        x='channel',
        y='reactivation_rate',
        hue='industry'
    )
    st.pyplot(fig2)

# 7. 数据下载
st.sidebar.download_button(
    label="Download Report (CSV)",
    data=filtered_df.to_csv().encode('utf-8'),
    file_name="reactivation_analysis.csv"
)