import streamlit as st
import yfinance as yf
import plotly.graph_objects as go # 匯入互動繪圖工具

st.title('📈 台股 K 線分析工具')

stock_id = st.text_input('請輸入台股代號', '2330')
target_stock = stock_id + '.TW'

# 抓取最近三個月的數據，畫 K 線圖會比較清楚
df = yf.Ticker(target_stock).history(period='3mo')

# 建立 K 線圖物件
fig = go.Figure(data=[go.Candlestick(
    x=df.index,
    open=df['Open'],
    high=df['High'],
    low=df['Low'],
    close=df['Close'],
    increasing_line_color='red', # 台灣習慣漲為紅
    decreasing_line_color='green' # 台灣習慣跌為綠
)])

# 設定圖表標題與手機適應性
fig.update_layout(
    title=f'{stock_id} 歷史 K 線圖',
    xaxis_rangeslider_visible=False # 隱藏下方的滑桿讓手機畫面更乾淨
)

# 在網頁上顯示圖表
st.plotly_chart(fig, use_container_width=True)

# 保留原本的數據表格供參考
st.subheader('數據細節')
st.write(df.tail())
