
import streamlit as st

st.set_page_config(layout="wide")

# txt1 = '**<p style="color:#9932cc;font-size: 50px;">作品紹介ページ</p>**'
# st.write(txt1, unsafe_allow_html=True)

st.markdown(
'<p><span style = "background-color:#ffb6c1;color:#ffffff;font-size: 30px;font-family:Kosugi Maru;"> ★　CoderDojo Tachikawa　★ </span></p>',
unsafe_allow_html=True)

for i in list(range(0,5)):
    path="./第40回/"
    path=path+str(i+1)
    st.header("NO."+str(i+1))
    st.image(f"{path}.JPG", use_column_width=True)
