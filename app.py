import streamlit as st
import yfinance as yf
import plotly.graph_objects as go

st.title('📈 台股 K 線分析工具')

# 1. 先定義滑桿 (一定要放在使用變數之前)
st.sidebar.header('設定參數')
ma_short = st.sidebar.slider('短期均線 (MA)', min_value=2, max_value=60, value=5)
ma_long = st.sidebar.slider('長期均線 (MA)', min_value=10, max_value=240, value=20)

stock_id = st.text_input('請輸入台股代號', '2330')
target_stock = stock_id + '.TW'

# 2. 抓取數據
df = yf.Ticker(target_stock).history(period='1y') # 改成 1y 才有足夠數據算長均線

# 3. 計算 MA
df['MA_S'] = df['Close'].rolling(window=ma_short).mean()
df['MA_L'] = df['Close'].rolling(window=ma_long).mean()

# 4. 繪製 K 線圖
fig = go.Figure(data=[go.Candlestick(
    x=df.index,
    open=df['Open'], high=df['High'],
    low=df['Low'], close=df['Close'],
    name='K線',
    increasing_line_color='red', # 漲設定為紅 🔴
    decreasing_line_color='blue'  # 跌設定為藍 🔵
)])

# 5. 加入動態均線
fig.add_trace(go.Scatter(x=df.index, y=df['MA_S'], name=f'{ma_short}MA', line=dict(color='orange', width=1)))
fig.add_trace(go.Scatter(x=df.index, y=df['MA_L'], name=f'{ma_long}MA', line=dict(color='blue', width=1)))

st.plotly_chart(fig, use_container_width=True)
