import streamlit as st
import random
from google.cloud import firestore
from google.oauth2 import service_account
import json
from PIL import Image

def toresult(q_sum, ans, right):
    index = st.session_state["answered"][q_sum]

    if ans==right:
        #ユーザの解答の登録
        st.session_state["correct"][index][0]=True       
    else:
        #ユーザの解答の登録
        st.session_state["correct"][index][0]=False
    st.session_state["correct"][index][1]=ans 
    #遷移先ページの明示
    st.session_state.pop("selectlist")
    st.session_state["page"]="result"

def get_data(quiz_id):
    key_dict = json.loads(st.secrets["textkey"])
    creds = service_account.Credentials.from_service_account_info(key_dict)
    db = firestore.Client(credentials=creds)
    doc_ref = db.collection("selection").document(str(quiz_id))
    # Then get the data at that reference.
    doc = doc_ref.get()
    return doc

def question():
    if not st.session_state:
        st.text("最初からやり直してください")
    else:
        q_sum=st.session_state["q_sum"]
        quiz_id = st.session_state["answered"][q_sum] # 現在の問題のデータベースのID
        
        # ここにデータベースからデータを引っ張り出す処理を入れたい
        doc = get_data(quiz_id)
        doc_dict = doc.to_dict()
        
        mistake_1 = doc_dict['mistake_1']
        mistake_2 = doc_dict['mistake_2']
        mistake_3 = doc_dict['mistake_3']
        right = doc_dict['right']
        
        st.text(quiz_id) # 現在の問題のデータベースのID
        st.text("この法律の内容を答えなさい")
        image = Image.open('./images/' + str(quiz_id) +'.png')
        st.image(image)

        if not 'selectlist' in st.session_state:
            selection_list=[mistake_1,mistake_2,mistake_3,right]
            random.shuffle(selection_list)
            st.session_state['selectlist'] = tuple(selection_list)

        ans=st.radio("この法律の内容を答えなさい",st.session_state['selectlist'],key="unchi")
        
        with st.form(key='profile_form'):
            st.form_submit_button("decide",on_click=toresult, args=[q_sum, ans, right])
        