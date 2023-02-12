import streamlit as st
import numpy as np
from google.cloud import firestore
from google.oauth2 import service_account
import json
from PIL import Image

def tostart():
    st.session_state["page"] = "start"

def finish():
#show answer
    st.text("ウンチ")
    for i in range(st.session_state["q_sum"]):
        # 答えた問題のデータベースのID
        nowq=st.session_state["answered"][i]
        #the answer which is correct or not that user selected
        if st.session_state["correct"][nowq][0]==False:
            ans="✕"
        elif st.session_state["correct"][nowq][0]==True:
            ans="〇"
        #the answer string that user selected
        ansstr=st.session_state["correct"][nowq][1]    
    
        #show answer
        st.text(f'{i+1};{ans};{ansstr}')
    st.button("STARTに戻る", key="backbtn", on_click=tostart)
