import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🎉 我的第一个生信可视化平台")
st.write("欢迎使用！这是一个简单的开始。")

# 上传文件功能
uploaded_file = st.file_uploader("上传CSV文件", type=['csv'])

chart_type = st.selectbox("选择图表类型", ["柱状图", "散点图", "箱线图"])

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

    # 新增：根据选择生成不同图表
    if chart_type == "柱状图":
        fig = px.bar(df, x=selected_categorical[0], y=selected_numeric[0])
    elif chart_type == "散点图":
        fig = px.scatter(df, x=selected_numeric[0], y=selected_numeric[1])
    
    st.plotly_chart(fig)
else:
    st.info("👈 请在左侧上传一个CSV文件")
