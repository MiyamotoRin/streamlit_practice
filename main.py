import streamlit as st
from google.cloud import firestore
from google.oauth2 import service_account
import json
import random
from PIL import Image

from pages.question import question
from pages.result import result
from pages.finish import finish

if 'page' not in st.session_state:
    st.session_state['page'] = 'start'

#ページのレイアウト諸々の設定
page_icon_image = Image.open('./AISpeculationQuiz_logo.jpg')
st.set_page_config(
    page_title= "AISpeculationQuiz",
    page_icon=page_icon_image,
    initial_sidebar_state="collapsed" #サイドバーを隠したい
    )

#initialize Session State
def init_SS():
    st.session_state["q_sum"] = 1 #回答数
    st.session_state["answered"] = list[int] #問題番号
    st.session_state["correct"] = dict[int,list[bool,str]] #keyが問題番号 valueは正誤とユーザの解答のリスト
    st.session_state["page"] = "start" #start question result finish

#出題する問題の番号をランダムに10個抽出する
#session_stateの問題番号のリストとcorrectを初期化
def num_random():
    num_set = set()
    while len(num_set) < 5: #繰り返し回数
        num_set.add(random.randint(1,15))
    numset = list(num_set) #リストに変換
    quedict = {}
    for i in range(len(numset)):
        quedict[numset[i]] = [False, ""]
    # 引っ張ってきた問題のデータベースのIDのリスト
    st.session_state["answered"] = numset 
    
    st.session_state["correct"] = quedict

def onStart():
    init_SS()
    num_random()
    #(問題を10問抽出する処理)#
    #(st.sessionに格納)
    st.session_state["page"] = "question"

#現在のpageの値によって描画する(実行する)関数が変わる
nowpage = st.session_state["page"]
if nowpage == "start":
    st.title('AI speculation quiz')
    st.text("Stable Diffusion で世界の面白い法律の問題を作りました")
    st.text("挑戦してみてください")
    start_style = """
            <style>
            p{
                font-size: 32px;
            }
            div.stButton {
                margin-top: 3%;
            }
            div.stButton > Button {
                padding: 0.50rem 2.00rem;
            }
            div[data-testid="stText"] {
                margin-top: 5%;
                font-size: 24px;
            }
            h1#ai-speculation-quiz { font-size: 700%; }
            h1#ai-speculation-quiz > div > a {
                display: none;
            }
            </style>
            """
    st.markdown(start_style, unsafe_allow_html=True)
    st.button("START",key="startbtn", on_click=onStart)
elif nowpage == "question":
    question()
elif nowpage == "result":
    result()
else:
    finish()

#共通のCSSの設定
hide_menu_style = """
        <style>
        #MainMenu {display: none;}
        .stActionButton {display: none;}
        div[data-testid="collapsedControl"] {display: none !important;}
        section[data-testid="stSidebar"] {display: none !important;}
        div[data-testid="stVerticalBlock"]{text-align: center}
        .block-container { margin-top: 5% }
        section.main > footer { display none; }

        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

