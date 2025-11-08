"""
このファイルは、Webアプリのメイン処理が記述されたファイルです。
This file contains the main logic for the web application.
"""

############################################################
# 1. ライブラリの読み込み
############################################################
import streamlit as st


############################################################
# 2. メイン画面表示の管理
############################################################
# ページ設定
st.set_page_config(
    page_title="ワンちゃん生活サポート", 
    page_icon="🐕", 
    layout="centered",
)
# ページ遷移の状態管理
if "page" not in st.session_state: 
    st.session_state["page"] = "ホーム🐾" # 初期画面をメニューに設定

# 各ページ定義
def main_menu(): 
    st.title("ミニチュアシュナウザーといっしょ")
    st.markdown("### ●●ちゃんの今日のようすを観察しよう！")
    st.write("メニューから操作したいものを選んでください。")

    # メニュー項目をグリッドで配置（2列）
    col1, col2 = st.columns(2)

    with col1: 
        if st.button(st.MENU1): 
            st.session_state["page"] = st.MENU1

        if st.button(st.MENU2): 
            st.session_state["page"] = st.MENU2
        if st.button(st.MENU3): 
            st.session_state["page"] = st.MENU3

    with col2: 
        if st.button(st.MENU4): 
            st.session_state["page"] = st.MENU4

        if st.button(st.MENU5): 
            st.session_state["page"] = st.MENU5

        if st.button(st.MENU6): 
            st.session_state["page"] = st.MENU6


############################################################
# 3. 初期化処理
############################################################



