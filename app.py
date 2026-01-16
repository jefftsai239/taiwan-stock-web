import streamlit as st

# 設定網頁標題
st.title('📈 我的台股分析工具')

# 顯示一段簡單的文字
st.write('歡迎來到我的雲端分析平台！這是一個專為手機設計的網頁介面。')

# 加入一個簡單的輸入框
stock_id = st.text_input('請輸入台股代號（例如：2330）', '2330')

st.write(f'你目前查看的股票是：{stock_id}')
