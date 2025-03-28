import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from faker import Faker

plt.style.use('seaborn-v0_8-whitegrid')  # 专业图表风格
sns.set_palette(["#1B8D4A", "#FF8000"])  # HelloFresh品牌色

# 生成假想数据（保险vs餐饮）
fake = Faker()
def generate_data():
    data = []
    for _ in range(200):
        data.append({
            'industry': 'insurance',
            'segment': fake.random_element(elements=('high_risk', 'medium_risk', 'low_risk')),
            'reactivation_rate': fake.random_int(min=15, max=45),
            'preferred_channel': fake.random_element(elements=('call', 'email', 'SMS'))
        })
        data.append({
            'industry': 'meal_kit',
            'segment': fake.random_element(elements=('vegan', 'family', 'gourmet')),
            'reactivation_rate': fake.random_int(min=25, max=60),
            'preferred_channel': fake.random_element(elements=('app_push', 'email', 'retargeting'))
        })
    return pd.DataFrame(data)

df = generate_data()

# 绘制对比条形图
plt.figure(figsize=(10, 6))
sns.barplot(x='industry', y='reactivation_rate', hue='segment', data=df, 
            palette=['#1B8D4A', '#FF8000', '#6ECB63'])  # HelloFresh色系
plt.title('Reactivation Rate by Industry/Segment', fontsize=14)
plt.xlabel('')
plt.ylabel('Reactivation Rate (%)')
plt.legend(title='Segment')
try:
    plt.savefig('d:/CHEN 作品集/HELLOfresh/reactivation_comparison.png', dpi=300, bbox_inches='tight')
    print("Successfully saved reactivation_comparison.png")
except Exception as e:
    print(f"Error saving reactivation_comparison.png: {e}")

# 生成RFM热力图（餐饮版）
rfm_data = pd.DataFrame({
    'recency': [3, 5, 1, 4, 2],
    'frequency': [5, 3, 4, 2, 5],
    'monetary': [120, 85, 90, 60, 150],
    'segment': ['loyalists', 'at_risk', 'potential', 'new', 'champions']
})

plt.figure(figsize=(8, 6))
sns.heatmap(rfm_data.set_index('segment'), annot=True, cmap='YlGn', 
           linewidths=0.5, fmt='g')  # 黄绿色系
plt.title('Meal Kit RFM Analysis', fontsize=12)
try:
    plt.savefig('d:/CHEN 作品集/HELLOfresh/rfm_heatmap.png', dpi=300, bbox_inches='tight')
    print("Successfully saved rfm_heatmap.png")
except Exception as e:
    print(f"Error saving rfm_heatmap.png: {e}")

# 添加交互式图表功能
from ipywidgets import interact

@interact(segment=['vegan', 'family', 'gourmet'])
def show_reactivation(segment):
    plt.figure(figsize=(8, 5))
    sns.barplot(data=df[df.segment==segment], 
               x='industry', 
               y='reactivation_rate',
               palette=['#1B8D4A', '#FF8000'])
    plt.title(f'Reactivation Rate for {segment} Segment')
    plt.ylabel('Reactivation Rate (%)')
    plt.show()
