import streamlit as st
st.session_state.number = 0

st.subheader("김태현이 즐겨타는 스타일은?")

if  "st.session_state.key" not in st.session_state:
    if st.button("프리스타일"):
        st.session_state.key = "프리스타일"
    if st.button("프리라이딩") :
        st.session_state.key = "프리라이딩"
    if st.button("다운힐") :
        st.session_state.key = "다운힐"
    
st.subheader("김태현이 보드를 타는 이유를 서술하시오")
st.session_state.text = st.text_input("20자 이내 띄어쓰기 없이")

st.subheader("학번을 입력하세요")
st.session_state.num = st.text_input("ex)1105")

st.subheader("이름을 입력하세요")
st.session_state.name = st.text_input("ex)김태현")

st.page_link("pages/1_print.py", label="다음")
            