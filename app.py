import streamlit as st 
import pandas as pd
view = [100,150,30]
st.write('# 학년별 학점')
st.write('## row')
view
st.write('## bar chart')
st.bar_chart(view) # bac_chart(데이터) : 데이터를 그래프로 표현
sview = pd.Series(view)
sview

