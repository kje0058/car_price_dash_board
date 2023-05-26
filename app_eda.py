import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def run_app_eda():

    st.subheader('데이터 분석')

    df=pd.read_csv('data/Car_Purchasing_Data.csv', encoding='ISO-8859-1')
    print(df)

    if st.checkbox('데이터 프레임 보기'):
        st.dataframe(df)

    st.subheader('기본 통계 데이터')

    st.dataframe(df.describe())

    st.subheader('최대 / 최소 데이터 확인하기')

    column = st.selectbox('최대/최소 데이터를 확인할 컬럼을 선택하세요.', df.columns[3:])

    st.text('최대 데이터')
    st.dataframe(df.loc[df[column]==df[column].max(),])

    st.text('최소 데이터')
    st.dataframe(df.loc[df[column]==df[column].min(),])

    st.subheader('컬럼 별 히스토그램')

    column = st.selectbox('히스토그램을 확인할 컬럼을 선택하세요.', df.columns[3:])
    bins = st.number_input('빈의 갯수를 입력하세요.', 10, 30, 20) # 최소.최대.기본값 // 히스토그램은 기본적으로 10개부터 보여주는게 맞음

    fig=plt.figure() # 영역을 먼저 잡아준다
    df[column].hist(bins=bins)

    plt.title(column + ' Histogram')
    plt.xlabel(column)
    plt.ylabel('count')

    st.pyplot(fig)

    st.subheader('상관관계 분석')
    column_list = st.multiselect('상관분석 하고싶은 컬럼을 선택하세요.', df.columns[3:])
    
    # df[column_list].corr() # 유저가 선택한 리스트만 상관계수를 보여주세요.
    # print(column_list) # 먼저 데이터 형태 확인

    if len(column_list)>=2:
        fig2=plt.figure()
        sns.heatmap(data=df[column_list].corr(), fmt='.2f', annot=True, vmin=-1, vmax=1, cmap='coolwarm', linewidths=0.3)
        st.pyplot(fig2)
    else:
        st.text('2개 이상 입력하세요.')