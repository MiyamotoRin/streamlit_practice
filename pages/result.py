import streamlit as st
from PIL import Image

def toque():
    st.session_state["page"]="question"

def tofin():
    st.session_state["page"]="finish"

def result():
    image = Image.open("images/sample.png")
    st.image(image)
    nowq = st.session_state["answered"][st.session_state["q_sum"]] #現在の問題を取得
    right = st.session_state["correct"][nowq] #現在の問題の正誤を取得
    st.text(nowq)
    st.text(right)
    # for i in 5:
    #     nowq=st.session_state["correct"][i]
    
    if right[0]: #正誤で表示する記号の処理
        st.text("〇")
    else:
        st.text("✕")
    st.text(right[1]) #正解
    if  int(st.session_state["q_sum"]) < 2:
        st.session_state["q_sum"] +=1
        st.button("NEXT", key="nextbtn", on_click=toque)
    else:
        st.button("END", key="endbtn", on_click=tofin)
        



