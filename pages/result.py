import streamlit as st
from google.cloud import firestore
from google.oauth2 import service_account
import json
from PIL import Image

def toque():
    st.session_state["page"]="question"

def tofin():
    st.session_state["page"]="finish"

def result():
    q_sum=st.session_state["q_sum"]
    quiz_id = st.session_state["answered"][q_sum] # 現在の問題のデータベースのID
    
    # ここにデータベースからデータを引っ張り出す処理を入れたい
    key_dict = json.loads(st.secrets["textkey"])
    creds = service_account.Credentials.from_service_account_info(key_dict)
    db = firestore.Client(credentials=creds)

    doc_ref = db.collection("quiz").document(str(quiz_id))
    # Then get the data at that reference.
    doc = doc_ref.get()
    doc_dict = doc.to_dict()  
    detail = doc_dict['detail'] #どこの国の法律か
    question = doc_dict['question']#答え

    image = Image.open("images/" + str(quiz_id) +".png")
    st.image(image)
    nowq = st.session_state["answered"][st.session_state["q_sum"]] #現在の問題を取得
    right = st.session_state["correct"][nowq] #現在の問題の正誤を取得
    
    if right[0]: #正誤で表示する記号の処理
        st.text("〇")
    else:
        st.text("✕")
    st.text(right[1]) #ユーザの回答
    st.text(f'正解は。。。{question}')
    st.text('解説')
    st.text(detail)
    
    #次のページ遷移処理(次の問題か問題終了か)
    if  int(st.session_state["q_sum"]) < 2:
        st.session_state["q_sum"] +=1
        st.button("NEXT", key="nextbtn", on_click=toque)
    else:
        st.button("END", key="endbtn", on_click=tofin)
        



