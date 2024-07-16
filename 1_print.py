import streamlit as st

st.write(
        st.session_state.num + st.session_state.name + "님의 점수는 "  
    )    
if st.session_state.key == "프리스타일" :
        st.session_state.number = 50
        if st.session_state.text == "낭만넘쳐서" :
            st.session_state.number = st.session_state.number+ 50
            
else :
    st.session_state.number = 0
    if st.session_state.text == "낭만넘쳐서" :
            st.session_state.number = st.session_state.number+ 50
     
     
st.subheader(st.session_state.number)
st.write("점입니다")