import streamlit as st
from PIL import Image

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