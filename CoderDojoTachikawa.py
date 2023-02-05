# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 10:00:36 2023

https://zenn.dev/ohtaman/articles/streamlit_tips

文字装飾
https://tradestation.life/blog/streamlit_unsafe_allow_html/

角丸
https://jajaaan.co.jp/web-production/frontend/border-radius/

任意の書式
https://zenn.dev/teruroom/scraps/15ea006d7b61fc

font-family: MS PMincho
font-family: Hiragino Maru Gothic Pro
font-family: M PLUS Rounded 1c
font-family: Kosugi Maru

@author: sa_tsukida
"""

import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="sttest", 
    page_icon='ccc.JPG', 
    layout="wide", 
    initial_sidebar_state="auto", 
    menu_items={
         'Get Help': 'https://www.google.com',
         'Report a bug': "https://www.google.com",
         'About': """
         # 画像生成風アプリ
         このアプリは画像生成風アプリで、実際にはキングスライムしか表示しません。
         """
     })

# link="https://picsum.photos/704/300?last"

f = open('myfile.txt', 'r', encoding='UTF-8')
data = f.read()
f.close()

def main():
    

    txt1 = '**<p style="color:#000000;font-size: 50px;">作品紹介ページ</p>**'
    st.write(txt1, unsafe_allow_html=True)

    # st.markdown(f"""
    # # 作品紹介ページ
    # """)

    # st.markdown(
    # '<p><span style = "background-color:#008080;color:#ffffff;font-size: 30px;font-family:Kosugi Maru;"> ★　CoderDojo Tachikawa　★ </span></p>',
    # unsafe_allow_html=True)

    logo="./main/dojologo.png"

    cols = st.columns(2)
    with cols[0]:
        # st.markdown("""\n""")        
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.markdown(
        '<p><span style = "background-color:#008080;color:#ffffff;font-size: 30px;font-family:Kosugi Maru;">★　CoderDojo Tachikawa　★ </span></p>',
        unsafe_allow_html=True)
    with cols[1]:
        st.image(f"{logo}", use_column_width=True)


    video_file = open('./main/myvideo.mp4', 'rb')
    video_bytes = video_file.read()

    st.video(video_bytes)

    # st.markdown(f"""
    # ![]({link})
    # """)

    st.write(data)
    


if __name__ == '__main__':
    main()