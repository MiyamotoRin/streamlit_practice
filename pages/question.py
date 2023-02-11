import streamlit as st
import numpy as np
from google.cloud import firestore
from google.oauth2 import service_account
import json
from PIL import Image

def toresult(q_sum, ans):
    index = st.session_state["answered"][q_sum]

    if ans=="a":
        #ユーザの解答の登録
        st.session_state["correct"][index][0]=True       
    else:
        #ユーザの解答の登録
        st.session_state["correct"][index][0]=False
    st.session_state["correct"][index][1]=ans 
    #遷移先ページの明示
    st.session_state["page"]="result"

def question():
    if not st.session_state:
        st.text("最初からやり直してください")
    else:
        q_sum=st.session_state["q_sum"]
        # ここにデータベースからデータを引っ張り出す処理を入れたい
        
        
        #仮version
        st.text(st.session_state["answered"][q_sum]) # 現在の問題のデータベースのID
        st.text("この法律の内容を答えなさい")
        image = Image.open('images/sample.png')
        st.image(image)
        ans=st.radio("この法律の内容を答えなさい",("a","b","c"),index=1)
        
        with st.form(key='profile_form'):
            st.form_submit_button("decide",on_click=toresult, args=[q_sum, ans])
        

        


                
        
    

    # with st.form(key='profile_form'):
    #     ans=st.radio(
    #         'この法律の内容を答えなさい',
    #         ('ワニを消火栓につないではいけない','ワニに水を飲ませてはいけない','ワニに背中を見せてはいけない')
    #     )

    #     submit_button = st.form_submit_button('送信')

    # if submit_button :
    #     if ans =='ワニを消火栓につないではいけない':
    #         st.text('正解！')
    #     else:
    #         st.text('だめぇぇぇ！')