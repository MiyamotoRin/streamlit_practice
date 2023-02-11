import streamlit as st
from google.cloud import firestore
from google.oauth2 import service_account
from PIL import Image
import json

key_dict = json.loads(st.secrets["textkey"])
creds = service_account.Credentials.from_service_account_info(key_dict)
db = firestore.Client(credentials=creds)

# Create a reference to quiz.
doc_ref = db.collection("quiz").document("1")

# Then get the data at that reference.
doc = doc_ref.get()

st.text(doc.to_dict()['statement'])

st.title('AI speculation quiz')
st.text('面白い法律をStableDiffusionで画像にしました。内容を推測してください')
image = Image.open('sample.png')
st.image(image)

with st.form(key='profile_form'):
    ans=st.radio(
        'この法律の内容を答えなさい',
        ('ワニを消火栓につないではいけない','ワニに水を飲ませてはいけない','ワニに背中を見せてはいけない')
    )

    submit_button = st.form_submit_button('送信')

if submit_button :
    if ans =='ワニを消火栓につないではいけない':
        st.text('正解！')
    else:
        st.text('だめぇぇぇ！')