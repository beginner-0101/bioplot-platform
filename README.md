# BioPlot - 生信数据可视化平台

## 🌟 项目简介
一个基于Streamlit的生信数据自动可视化平台，支持上传基因表达矩阵、差异分析结果等数据，一键生成高质量图表。

## 🚀 功能特点
- 📁 支持多种格式：CSV、TSV、Excel
- 📊 智能列识别：自动区分数值列和分类列
- 🎨 多种图表：柱状图、散点图、箱线图、直方图
- 📥 导出功能：HTML交互图表、PNG图片、CSV数据
- 🧹 数据预处理：空值处理、简单统计

## 🔧 快速开始

### 本地运行
```bash
# 1. 克隆项目
git clone https://github.com/beginner-0101/bioplot-platform.git
cd bioplot-platform

# 2. 创建虚拟环境
python -m venv venv
venv\Scripts\activate.bat  # Windows
source venv/bin/activate   # Mac/Linux

# 3. 安装依赖
pip install -r requirements.txt

# 4. 运行应用
streamlit run app.py