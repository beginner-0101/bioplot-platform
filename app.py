import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="BioPlot - 生信可视化平台",
    page_icon="📊",
    layout="wide"
)

st.title("📊 BioPlot - 生信数据可视化平台")
st.write("欢迎使用！上传你的生信数据，自动生成可视化图表。")

# 上传文件功能
uploaded_file = st.file_uploader("上传CSV文件", type=['csv'])

if uploaded_file is not None:
    # 读取数据
    df = pd.read_csv(uploaded_file)
    
    # 显示在左侧边栏
    with st.sidebar:
        st.header("📊 图表设置")
        
        chart_type = st.selectbox("选择图表类型", ["柱状图", "散点图", "箱线图", "直方图"])
        
        # 自动识别列类型
        numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
        categorical_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()
        
        # 让用户选择列
        if chart_type == "柱状图":
            x_col = st.selectbox("选择X轴（分类列）", categorical_cols if categorical_cols else ["无分类列"])
            y_col = st.selectbox("选择Y轴（数值列）", numeric_cols)
            
        elif chart_type == "散点图":
            x_col = st.selectbox("选择X轴", numeric_cols)
            y_col = st.selectbox("选择Y轴", [col for col in numeric_cols if col != x_col])
            color_col = st.selectbox("按颜色分组（可选）", ["无"] + categorical_cols)
            
        elif chart_type == "箱线图":
            x_col = st.selectbox("选择分组列", categorical_cols if categorical_cols else ["无分类列"])
            y_col = st.selectbox("选择数值列", numeric_cols)
            
        elif chart_type == "直方图":
            col_for_hist = st.selectbox("选择要分析的列", numeric_cols)
            bins = st.slider("选择分组数", min_value=5, max_value=100, value=30)
    
    # 主内容区 - 显示数据信息
    st.write("### 数据预览")
    st.dataframe(df.head(), use_container_width=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("行数（样本）", df.shape[0])
    with col2:
        st.metric("列数（变量）", df.shape[1])
    with col3:
        st.metric("数值列数量", len(numeric_cols))
    
    # 根据选择生成图表
    st.write("---")
    st.write("## 📈 数据可视化")
    
    fig = None
    
    if chart_type == "柱状图":
        if x_col != "无分类列":
            # 按分类计算平均值
            agg_df = df.groupby(x_col)[y_col].mean().reset_index()
            fig = px.bar(
                agg_df, 
                x=x_col, 
                y=y_col,
                title=f"{y_col} 按 {x_col} 的平均值",
                color=x_col
            )
                
    elif chart_type == "散点图":
        fig = px.scatter(
            df,
            x=x_col,
            y=y_col,
            color=color_col if color_col != "无" else None,
            title=f"{y_col} vs {x_col}"
        )
            
    elif chart_type == "箱线图":
        if x_col != "无分类列":
            fig = px.box(
                df,
                x=x_col,
                y=y_col,
                title=f"{y_col} 按 {x_col} 的分布",
                color=x_col
            )
                
    elif chart_type == "直方图":
        fig = px.histogram(
            df,
            x=col_for_hist,
            nbins=bins,
            title=f"{col_for_hist} 的分布"
        )
    
    # 显示图表和下载按钮
    if fig is not None:
        st.plotly_chart(fig, use_container_width=True)
        
        # 下载按钮
        col1, col2, col3 = st.columns(3)
        with col1:
            png_image = fig.to_image(format="png")
            st.download_button(
                label="📥 下载PNG",
                data=png_image,
                file_name="chart.png",
                mime="image/png"
            )
        with col2:
            html_content = fig.to_html()
            st.download_button(
                label="📥 下载HTML",
                data=html_content,
                file_name="chart.html",
                mime="text/html"
            )
        with col3:
            csv = df.to_csv(index=False)
            st.download_button(
                label="📊 下载数据",
                data=csv,
                file_name="data.csv",
                mime="text/csv"
            )

else:
    # 未上传文件时的展示
    st.info("👈 请上传CSV文件开始分析")
    
    # 示例展示
    st.write("### 支持的数据格式：")
    st.write("- 基因表达矩阵")
    st.write("- 差异分析结果")
    st.write("- 样本特征数据")

# 页脚
st.write("---")
st.caption("BioPlot v1.0 | 生信数据可视化平台")