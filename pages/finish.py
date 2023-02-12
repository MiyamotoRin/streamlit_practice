import streamlit as st
import numpy as np
import pandas as pd
from google.cloud import firestore
from google.oauth2 import service_account
import json
from PIL import Image

def tostart():
    st.session_state["page"] = "start"

def finish():
#show answer
    correct_count=0
    for i in range(st.session_state["q_sum"]):
        nowq=st.session_state["answered"][i + 1]
        if st.session_state["correct"][nowq][0]==True:
            correct_count+=1
    st.title("結果発表")
    st.header(f'あなたは{st.session_state["q_sum"]}問中{correct_count}問正解です')
    #st.subheader("あなたの解答")  
    
    result_list=[]
    for i in range(st.session_state["q_sum"]):
        # 答えた問題のデータベースのID
        nowq=st.session_state["answered"][i + 1]
        #the answer which is correct or not that user selected
        if st.session_state["correct"][nowq][0]==False:
            ans="✕"
        elif st.session_state["correct"][nowq][0]==True:
            ans="〇"
        #the answer string that user selected 
        ansstr=st.session_state["correct"][nowq][1]    
        ans_list=[ans,ansstr]
        #show answer
        result_list.append(ans_list)
        # st.text(f'{i+1}問目：{ans}{ansstr}')
        
    df = pd.DataFrame(
        result_list,
        index=(f'{i+1}問目' for i in range(len(result_list))),
        columns=('正誤',"あなたの解答"))
    st.dataframe(df,width=800)
    
    st.button("STARTに戻る", key="backbtn", on_click=tostart)
