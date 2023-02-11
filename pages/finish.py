import streamlit as st
import numpy as np
from google.cloud import firestore
from google.oauth2 import service_account
import json
from PIL import Image

def finish():
#show answer
    for i in st.session_state["answered"]:
        #the database ID of the question
        que_num=st.session_state["correct"][i].key
        #the answer which is correct or not that user selected
        if st.session_state["correct"][i].value[0]==False:
            ans="✕"
        elif st.session_state["correct"][i].value[0]==True:
            ans="〇"
        #the answer string that user selected
        ansstr=st.session_state["correct"][i].value[1]    
    
        #show answer
        st.text(i)
        st.text(";")
        st.text(ans)
        st.text(";")
        st.text(ansstr)
    
    
    