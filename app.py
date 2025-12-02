import streamlit as st
import pandas as pd

st.title("🎉 我的第一个生信可视化平台")
st.write("欢迎使用！这是一个简单的开始。")

# 上传文件功能
uploaded_file = st.file_uploader("上传CSV文件", type=['csv'])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("### 数据预览")
    st.dataframe(df.head())
    
    st.write("### 基本信息")
    st.write(f"- 行数: {df.shape[0]}")
    st.write(f"- 列数: {df.shape[1]}")
    
    # 简单的统计
    st.write("### 数值列统计")
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    for col in numeric_cols[:3]:  # 显示前3列
        st.write(f"**{col}**: 均值={df[col].mean():.2f}")
else:
    st.info("👈 请在左侧上传一个CSV文件")