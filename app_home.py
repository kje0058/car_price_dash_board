import streamlit as st


def run_app_home():
    st.subheader('안녕하세요~!^^')
    st.text('좋은 서비스로 보답하겠습니다.')
    st.text('자동 배포 처리된 앱입니다!!!!!')

    st.text('이 앱은 고객 데이터와 자동차 구매 데이터에 대한 내용입니다.')
    st.text('데이터 분석도 가능하고, 고객 정보를 넣으면 구매 차량 가격도 예측해줍니다.')

    img_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQqDF3aFQ9odxx5GY_HHFlIIighDfPrSjpe6w&usqp=CAU'
    st.image(img_url,width=800)