import streamlit as st
st.title("What is board")
st.divider()
st.image('longboard.jpg')
st.subheader("롱보드는 스케이트보드의 한 종류로써 데크가 긴 형태의 보드를 말합니다.")
st.subheader("길이가 긴 특성때문에 여러 스타일이있습니다.")
st.divider()
with st.container():
    st.image('hill.jpg')
    st.write("다운힐 : 무조건적 속도를 올려 내려오는 스타일")
    st.image('style.png')
    st.write("프리스타일 : 평지에서 댄싱과 트릭을 하며 타는 스타일")
    st.image('ride.jpg')
    st.write("프리라이드 : 속도를 올려 타는 다운힐과 달리 중간중간 슬라이드라는 트릭을 이용하는 스타일")
